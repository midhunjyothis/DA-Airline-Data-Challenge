import pandas as pd


def calculate_route_costs(
    route_flights: pd.DataFrame,
    flights_enriched: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate route-level operating costs based on distance, airport fees,
    and delay-related penalties.

    Notes
    -----
    - Cancelled flights are excluded.
    - Routes are unordered airport pairs (AIRPORT_A, AIRPORT_B).
    - Delay costs apply per leg:
        max(DEP_DELAY - 15, 0) * 75 + max(ARR_DELAY - 15, 0) * 75
    - Airport fees are per landing (destination airport), but for a round trip
      there are two landings (one at each airport). We compute per-route fees
      using airport types attached to each leg.
    """
    required_route_cols = {"AIRPORT_A", "AIRPORT_B", "flight_legs", "total_distance", "roundtrip_flights"}
    missing_route = required_route_cols - set(route_flights.columns)
    if missing_route:
        raise ValueError(f"route_flights missing required columns: {sorted(missing_route)}")

    required_flight_cols = {
        "ORIGIN",
        "DESTINATION",
        "CANCELLED",
        "DISTANCE",
        "DEP_DELAY",
        "ARR_DELAY",
        "ORIGIN_AIRPORT_TYPE",
        "DEST_AIRPORT_TYPE",
    }
    missing_f = required_flight_cols - set(flights_enriched.columns)
    if missing_f:
        raise ValueError(f"flights_enriched missing required columns: {sorted(missing_f)}")

    f = flights_enriched.copy()
    f = f[f["CANCELLED"] == 0]

    # route normalization
    f["AIRPORT_A"] = f[["ORIGIN", "DESTINATION"]].min(axis=1)
    f["AIRPORT_B"] = f[["ORIGIN", "DESTINATION"]].max(axis=1)

    # numeric coercions
    f["DISTANCE"] = pd.to_numeric(f["DISTANCE"], errors="coerce")
    f["DEP_DELAY"] = pd.to_numeric(f["DEP_DELAY"], errors="coerce").fillna(0)
    f["ARR_DELAY"] = pd.to_numeric(f["ARR_DELAY"], errors="coerce").fillna(0)

    # delay cost per leg
    dep_billable = (f["DEP_DELAY"] - 15).clip(lower=0)
    arr_billable = (f["ARR_DELAY"] - 15).clip(lower=0)
    f["delay_cost"] = (dep_billable + arr_billable) * 75

    # airport fee per leg = fee at destination airport
    def _airport_fee(airport_type: pd.Series) -> pd.Series:
        # using challenge wording: medium=$5k, large=$10k
        return airport_type.map({"medium_airport": 5000, "large_airport": 10000})

    f["dest_airport_fee"] = _airport_fee(f["DEST_AIRPORT_TYPE"])

    per_route = (
        f.groupby(["AIRPORT_A", "AIRPORT_B"], as_index=False)
        .agg(
            total_delay_cost=("delay_cost", "sum"),
            total_airport_fees=("dest_airport_fee", "sum"),
        )
    )

    # distance-based cost (9.18 per mile) uses route_flights total_distance
    costs = route_flights.merge(per_route, on=["AIRPORT_A", "AIRPORT_B"], how="left")

    costs["total_delay_cost"] = costs["total_delay_cost"].fillna(0)
    costs["total_airport_fees"] = costs["total_airport_fees"].fillna(0)

    costs["total_distance_cost"] = costs["total_distance"] * 9.18
    costs["total_cost"] = costs["total_distance_cost"] + costs["total_airport_fees"] + costs["total_delay_cost"]

    return costs[
        [
            "AIRPORT_A",
            "AIRPORT_B",
            "roundtrip_flights",
            "flight_legs",
            "total_distance",
            "total_distance_cost",
            "total_airport_fees",
            "total_delay_cost",
            "total_cost",
        ]
    ]

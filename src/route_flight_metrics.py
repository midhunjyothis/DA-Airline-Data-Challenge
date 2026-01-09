import pandas as pd


def aggregate_route_flights(flights: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate flight data to the round-trip route level.

    A route is defined as an unordered airport pair.
    Cancelled flights are excluded.
    """
    required_cols = {
        "ORIGIN",
        "DESTINATION",
        "CANCELLED",
        "DISTANCE",
        "DEP_DELAY",
        "ARR_DELAY",
    }
    missing = required_cols - set(flights.columns)
    if missing:
        raise ValueError(f"Flights dataset missing required columns: {sorted(missing)}")

    f = flights.copy()

    # exclude cancelled flights
    f = f[f["CANCELLED"] == 0]

    # normalize unordered route
    route_df = (
        pd.DataFrame(
            {
                "AIRPORT_A": f[["ORIGIN", "DESTINATION"]].min(axis=1),
                "AIRPORT_B": f[["ORIGIN", "DESTINATION"]].max(axis=1),
            }
        )
        .assign(
            DISTANCE=pd.to_numeric(f["DISTANCE"], errors="coerce"),
            DEP_DELAY=pd.to_numeric(f["DEP_DELAY"], errors="coerce").fillna(0),
            ARR_DELAY=pd.to_numeric(f["ARR_DELAY"], errors="coerce").fillna(0),
        )
    )

    agg = (
        route_df.groupby(["AIRPORT_A", "AIRPORT_B"], as_index=False)
        .agg(
            flight_legs=("DISTANCE", "size"),
            total_distance=("DISTANCE", "sum"),
            total_dep_delay=("DEP_DELAY", "sum"),
            total_arr_delay=("ARR_DELAY", "sum"),
        )
    )

    # round trips = two legs
    agg["roundtrip_flights"] = agg["flight_legs"] // 2

    return agg

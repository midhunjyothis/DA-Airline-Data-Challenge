import pandas as pd


def calculate_route_revenue(
    route_flights: pd.DataFrame,
    ticket_prices: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate route-level revenue using ticket fares, occupancy proxy, and baggage assumptions.

    Revenue model (per round trip):
    - Ticket revenue: avg_roundtrip_fare * (avg passengers per round trip)
      where passengers per round trip is approximated as:
        200 seats * avg occupancy rate (route-level)  [handled upstream via feature engineering later]
      For this step, revenue uses only ticket fare + baggage fee mechanics and expects
      an input column 'avg_occupancy_rate' to already exist on route_flights if used.

    - Baggage revenue:
        200 seats * avg_occupancy_rate * 50% bags * $35 per bag per leg * 2 legs per round trip
      => passengers * 0.5 * 35 * 2

    Notes:
    - ticket_prices is sampled; results are directional.
    - This function does not infer occupancy from Tickets.
    """
    required_route_cols = {"AIRPORT_A", "AIRPORT_B", "roundtrip_flights"}
    missing_route = required_route_cols - set(route_flights.columns)
    if missing_route:
        raise ValueError(f"route_flights missing required columns: {sorted(missing_route)}")

    required_ticket_cols = {"ORIGIN", "DESTINATION", "avg_roundtrip_fare"}
    missing_ticket = required_ticket_cols - set(ticket_prices.columns)
    if missing_ticket:
        raise ValueError(f"ticket_prices missing required columns: {sorted(missing_ticket)}")

    rf = route_flights.copy()

    # Expect occupancy rate feature later; for now default to NaN if not provided.
    if "avg_occupancy_rate" not in rf.columns:
        rf["avg_occupancy_rate"] = pd.NA

    # Join ticket prices in both directions by creating a normalized (unordered) key for tickets
    tp = ticket_prices.copy()
    tp["AIRPORT_A"] = tp[["ORIGIN", "DESTINATION"]].min(axis=1)
    tp["AIRPORT_B"] = tp[["ORIGIN", "DESTINATION"]].max(axis=1)
    tp = tp.groupby(["AIRPORT_A", "AIRPORT_B"], as_index=False).agg(
        avg_roundtrip_fare=("avg_roundtrip_fare", "mean")
    )

    revenue = rf.merge(tp, on=["AIRPORT_A", "AIRPORT_B"], how="left")

    # passengers per round trip requires occupancy; keep components explicit
    seats_per_flight = 200
    revenue["passengers_per_leg"] = seats_per_flight * revenue["avg_occupancy_rate"]
    revenue["passengers_per_roundtrip"] = revenue["passengers_per_leg"] * 2

    revenue["ticket_revenue_per_roundtrip"] = revenue["avg_roundtrip_fare"] * revenue["passengers_per_roundtrip"]

    # baggage: 50% check 1 bag per leg; $35 per bag per leg
    revenue["baggage_revenue_per_roundtrip"] = revenue["passengers_per_roundtrip"] * 0.5 * 35

    revenue["revenue_per_roundtrip"] = (
        revenue["ticket_revenue_per_roundtrip"] + revenue["baggage_revenue_per_roundtrip"]
    )

    revenue["total_revenue"] = revenue["revenue_per_roundtrip"] * revenue["roundtrip_flights"]

    return revenue[
        [
            "AIRPORT_A",
            "AIRPORT_B",
            "roundtrip_flights",
            "avg_roundtrip_fare",
            "avg_occupancy_rate",
            "passengers_per_roundtrip",
            "ticket_revenue_per_roundtrip",
            "baggage_revenue_per_roundtrip",
            "revenue_per_roundtrip",
            "total_revenue",
        ]
    ]

import pandas as pd


def calculate_route_profit(
    route_costs: pd.DataFrame,
    route_revenue: pd.DataFrame,
) -> pd.DataFrame:
    """
    Combine route-level costs and revenue to compute profit.

    Returns one row per route (AIRPORT_A, AIRPORT_B) with:
    total_revenue, total_cost, profit, plus key components.
    """
    required_cost_cols = {
        "AIRPORT_A",
        "AIRPORT_B",
        "roundtrip_flights",
        "total_distance_cost",
        "total_airport_fees",
        "total_delay_cost",
        "total_cost",
    }
    missing_c = required_cost_cols - set(route_costs.columns)
    if missing_c:
        raise ValueError(f"route_costs missing required columns: {sorted(missing_c)}")

    required_rev_cols = {
        "AIRPORT_A",
        "AIRPORT_B",
        "roundtrip_flights",
        "avg_roundtrip_fare",
        "total_revenue",
        "ticket_revenue_per_roundtrip",
        "baggage_revenue_per_roundtrip",
        "revenue_per_roundtrip",
    }
    missing_r = required_rev_cols - set(route_revenue.columns)
    if missing_r:
        raise ValueError(f"route_revenue missing required columns: {sorted(missing_r)}")

    df = route_costs.merge(
        route_revenue[
            [
                "AIRPORT_A",
                "AIRPORT_B",
                "roundtrip_flights",
                "avg_roundtrip_fare",
                "ticket_revenue_per_roundtrip",
                "baggage_revenue_per_roundtrip",
                "revenue_per_roundtrip",
                "total_revenue",
            ]
        ],
        on=["AIRPORT_A", "AIRPORT_B", "roundtrip_flights"],
        how="left",
    )

    # If ticket fares are missing for a route (sample data gap), profit can't be computed reliably.
    df["profit"] = df["total_revenue"] - df["total_cost"]

    return df[
        [
            "AIRPORT_A",
            "AIRPORT_B",
            "roundtrip_flights",
            "avg_roundtrip_fare",
            "ticket_revenue_per_roundtrip",
            "baggage_revenue_per_roundtrip",
            "total_revenue",
            "total_distance_cost",
            "total_airport_fees",
            "total_delay_cost",
            "total_cost",
            "profit",
        ]
    ]

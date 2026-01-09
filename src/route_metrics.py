import pandas as pd

def aggregate_ticket_prices(tickets: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate ticket data to the route level for use in profitability analysis.

    Output grain: one row per directional route (ORIGIN, DESTINATION).
    Only round-trip itineraries in 1Q2019 are included.
    """
    required_cols = {"YEAR", "QUARTER", "ROUNDTRIP", "ORIGIN", "DESTINATION", "ITIN_FARE", "PASSENGERS"}
    missing = required_cols - set(tickets.columns)
    if missing:
        raise ValueError(f"Tickets dataset missing required columns: {sorted(missing)}")

    t = tickets.copy()

    # filters per challenge instructions
    t = t[(t["YEAR"] == 2019) & (t["QUARTER"] == 1) & (t["ROUNDTRIP"] == 1)]

    # coerce fare to numeric; drop unusable rows
    t["ITIN_FARE"] = pd.to_numeric(t["ITIN_FARE"], errors="coerce")
    t = t.dropna(subset=["ITIN_FARE", "PASSENGERS", "ORIGIN", "DESTINATION"])

    agg = (
        t.groupby(["ORIGIN", "DESTINATION"], as_index=False)
        .agg(
            avg_roundtrip_fare=("ITIN_FARE", "mean"),
            ticket_record_count=("ITIN_FARE", "size"),
            sample_passengers=("PASSENGERS", "sum"),
        )
    )

    return agg

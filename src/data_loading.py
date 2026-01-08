from __future__ import annotations

import os
import pandas as pd


def _require_file(path: str) -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")


def load_and_join_data(
    flights_path: str,
    tickets_path: str,
    airports_path: str,
):
    """
    Load source datasets. Joining is intentionally separated from loading so that
    schema and quality checks can be performed on raw inputs.

    Returns raw dataframes: (flights, tickets, airports).
    """
    _require_file(flights_path)
    _require_file(tickets_path)
    _require_file(airports_path)

    flights = pd.read_csv(flights_path, low_memory=False)
    tickets = pd.read_csv(tickets_path, low_memory=False)
    airports = pd.read_csv(airports_path, low_memory=False)

    return flights, tickets, airports

def add_airport_eligibility(
    flights: pd.DataFrame,
    airports: pd.DataFrame,
) -> pd.DataFrame:
    """
    Enrich flights with airport eligibility information by attaching
    airport type data for both origin and destination airports.
    """
    airports_ref = airports[
        airports["IATA_CODE"].notna()
    ][["IATA_CODE", "TYPE"]].drop_duplicates()

    flights = flights.merge(
        airports_ref,
        left_on="ORIGIN",
        right_on="IATA_CODE",
        how="left",
    ).rename(columns={"TYPE": "ORIGIN_AIRPORT_TYPE"}).drop(columns=["IATA_CODE"])

    flights = flights.merge(
        airports_ref,
        left_on="DESTINATION",
        right_on="IATA_CODE",
        how="left",
    ).rename(columns={"TYPE": "DEST_AIRPORT_TYPE"}).drop(columns=["IATA_CODE"])

    return flights


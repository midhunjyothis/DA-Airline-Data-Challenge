# Join Strategy

## Primary Dataset
- **Flights.csv** is the primary dataset. It contains flight-leg level operations (cancellations, delays, distance/air time) and the occupancy rate required for revenue modeling.

## Supporting Datasets
- **Airport_Codes.csv** is used only to determine airport eligibility (medium / large). It is not a source of metrics.
- **Tickets.csv** is treated as a pricing signal only (sample data). It is not used for occupancy and not assumed to represent full revenue coverage.

## Join Keys
- **Flights ↔ Airport Codes**
  - `Flights.ORIGIN` - `Airport_Codes.IATA_CODE`
  - `Flights.DESTINATION` - `Airport_Codes.IATA_CODE`

- **Flights ↔ Tickets**
  - Join on route endpoints using IATA codes:
    - `Flights.ORIGIN + Flights.DESTINATION`
    - `Tickets.ORIGIN + Tickets.DESTINATION`
  - Tickets are filtered to `YEAR = 2019`, `QUARTER = 1`, and `ROUNDTRIP = 1` prior to aggregation.

## Join Direction
- Start from **Flights** and left-join reference data.
  - Airport Codes is joined twice (origin and destination) to support eligibility filtering.
  - Tickets are aggregated to the route level and then joined, avoiding any implication that itinerary-level prices map directly to individual flight legs.

## Assumptions
- Flights is the authoritative source for which routes operated and their operational performance in 1Q2019.
- Airport Codes is authoritative for airport eligibility, but only rows with valid IATA codes are usable.
- Tickets data is sampled; fare-based revenue derived from it is treated as directional.

## Known Limitations
- Ticket data is itinerary-level and sampled, introducing coverage bias at the route level.
- Some airports present in Flights may not match Airport Codes due to missing IATA codes.
- Joining ticket prices at the route level ignores within-route variation (carrier, timing), which is acceptable for initial route screening.

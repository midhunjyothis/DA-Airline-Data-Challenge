# Step 3 — Join Strategy

## Primary Dataset
- Flights.csv is the primary dataset. It is the only dataset that has flight-leg level operations (cancellations, delays, distance/air time) and the occupancy rate required for passenger revenue.

## Supporting Datasets
- Airport_Codes.csv is used to determine whether an airport should be considered in-scope (medium/large only). This is an eligibility filter, not a metric source.
- Tickets.csv is treated as a ticket price signal only (sample data). It is not treated as full revenue coverage and is not used for occupancy.

## Join Keys
- Flights ↔ Airport Codes: join on airport IATA code.
  - `Flights.ORIGIN` ↔ `Airport_Codes.IATA_CODE`
  - `Flights.DESTINATION` ↔ `Airport_Codes.IATA_CODE`
  
- Flights ↔ Tickets: join on route endpoints, using IATA codes.
  - `Flights.ORIGIN` + `Flights.DESTINATION` ↔ `Tickets.ORIGIN` + `Tickets.DESTINATION`
  - Tickets must be filtered to `YEAR = 2019`, `QUARTER = 1`, and `ROUNDTRIP = 1`.

## Join Direction
- Start from Flights and left-join in reference information.
  - Airport Codes: left-join twice (once for origin, once for destination) to bring in airport type/size classification inputs.
  - Tickets: left-join aggregated ticket pricing to route pairs (not to individual flight legs), to avoid implying itinerary-level prices map 1:1 to specific flights.

## Key Assumptions
- The Flights dataset is treated as the authoritative source for which routes existed and how they performed operationally in 1Q2019.
- Airport Codes is treated as the authoritative source for airport eligibility, but only rows with valid IATA codes are usable for matching.
- Tickets is sample data; fare-based revenue derived from Tickets is treated as an estimate and is not assumed to represent full market revenue.

## Known Limitations
- Ticket records are itinerary-level and sampled, so any route-level pricing derived from Tickets has coverage bias risk.
- Some airports in Flights may not match to Airport Codes due to missing IATA codes in the reference table.
- Joining Tickets at the route level ignores within-route variation by carrier, day, or time; this is acceptable for a first-pass route screening but should be called out in conclusions.

# Ticket Price Aggregation Strategy

## Purpose
Use the Tickets dataset to derive a reasonable route-level ticket price signal that can be combined with flight-level operational data to estimate revenue. This aggregation is intended for route screening and comparison, not precise revenue accounting.

## Unit of Aggregation
- Route-level, defined as an unordered airport pair (origin, destination).
- Ticket data is aggregated across all round-trip itineraries for the same route in 1Q2019.

## Filters Applied
- YEAR = 2019
- QUARTER = 1
- ROUNDTRIP = 1
- Records with missing ITIN_FARE or PASSENGERS are excluded from aggregation.

## Metrics Produced
- Average round-trip ticket fare per route
- Total observed passengers in the sample (for context only)
- Count of ticket records contributing to the route-level estimate

## How This Will Be Joined to Flights
- Ticket metrics are joined to flight data at the route level using origin and destination IATA codes.
- Ticket prices are treated as a route-level attribute and are not mapped to individual flight legs.
- Occupancy is taken exclusively from the Flights dataset, not inferred from Tickets.

## Key Assumptions
- Ticket prices are assumed to be stable within the quarter, as instructed.
- Sample ticket data provides a directional pricing signal, even though it does not represent full market coverage.
- Average fare is a more stable signal than max or min fare for early-stage route selection.

## Known Limitations
- Ticket data is sampled and itinerary-based, not exhaustive.
- Pricing variation by carrier, day, or time of travel is not modeled.
- Passenger counts from Tickets are not used to infer flight-level demand.
- Revenue estimates derived from this data should be treated as approximations.

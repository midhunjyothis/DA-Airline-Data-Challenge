# Ticket Price Aggregation Strategy

## Purpose
Derive a route-level ticket price signal from the Tickets dataset that can be combined with flight-level operational data for revenue estimation. This is intended for route screening, not precise revenue accounting.

## Unit of Aggregation
- Route-level, defined as an unordered airport pair.
- Aggregation includes all round-trip itineraries for the same route in 1Q2019.

## Filters Applied
- `YEAR = 2019`
- `QUARTER = 1`
- `ROUNDTRIP = 1`
- Records with missing `ITIN_FARE` or `PASSENGERS` are excluded.

## Metrics Produced
- Average round-trip fare per route
- Ticket record count per route
- Observed passenger count (context only)

## Join to Flights
- Ticket metrics are joined to flight data at the route level using origin and destination IATA codes.
- Ticket prices are treated as route attributes and are not mapped to individual flight legs.
- Occupancy is sourced only from the Flights dataset.

## Assumptions
- Ticket prices are stable within the quarter, per problem instructions.
- Sample ticket data provides a directional pricing signal.
- Average fare is preferred over extremes for early-stage route comparison.

## Limitations
- Ticket data is sampled and itinerary-level.
- Pricing variation by carrier, day, or time is not modeled.
- Passenger counts from Tickets are not used to infer flight-level demand.
- Revenue estimates should be treated as approximations.

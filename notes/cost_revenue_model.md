# Cost & Revenue Model (Route Level)

## Scope
- Computed at the round-trip route level using 1Q2019 flight activity.
- Cancelled flights are excluded.
- Each route is assumed to be served by one dedicated aircraft.

## Cost Components
- **Distance-based operating costs**
  - Fuel, maintenance, crew: $8 per mile
  - Depreciation, insurance, other: $1.18 per mile
  - Total: $9.18 per mile

- **Airport fees**
  - $10,000 per landing at large airports
  - $5,000 per landing at medium airports
  - Two landings per round trip

- **Delay costs**
  - First 15 minutes free for departures and arrivals
  - $75 per minute beyond the grace period
  - Applied separately to departure and arrival delays

## Revenue Components
- **Ticket revenue**
  - Average round-trip fare derived from Tickets data
  - Applied at the route level

- **Baggage revenue**
  - $35 per checked bag per flight leg
  - 50% of passengers check one bag
  - Two legs per round trip

## Units & Grain
- Costs and revenue are calculated per round trip.
- Quarterly totals are derived using completed round-trip counts.

## Assumptions
- Occupancy from the Flights dataset reflects passenger load.
- Ticket prices are stable within the quarter.
- Delay costs increase linearly beyond the grace period.
- Baggage behavior is consistent across routes.

## Limitations
- Ticket pricing is based on sampled itinerary data.
- Costs do not vary by aircraft utilization beyond route assignment.
- No adjustment for directional imbalance or seasonality.

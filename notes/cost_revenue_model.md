# Cost & Revenue Model (Route Level)

## Scope
- Calculated at the round-trip route level using 1Q2019 flight activity.
- Only completed flights are considered; cancelled flights are excluded.
- Each route is assumed to be served by one dedicated aircraft.

## Cost Components
- **Distance-based operating costs**
  - Fuel, oil, maintenance, crew: $8 per mile
  - Depreciation, insurance, other: $1.18 per mile
  - Total variable operating cost: $9.18 per mile
- **Airport operational fees**
  - $10,000 per landing at large airports
  - $5,000 per landing at medium airports
  - Two landings per round trip (one at each airport)
- **Delay-related costs**
  - First 15 minutes free for departures and arrivals
  - Each additional minute costs $75
  - Applied separately to departure and arrival delays

## Revenue Components
- **Ticket revenue**
  - Average round-trip fare derived from the Tickets dataset
  - Applied at the route level, not per individual flight
- **Baggage revenue**
  - $35 per checked bag per flight leg
  - 50% of passengers check one bag
  - Two legs per round trip

## Units & Grain
- Costs and revenue are computed per round-trip.
- Quarterly totals are derived by multiplying per–round-trip economics by the number of completed round trips for each route.

## Key Assumptions
- Occupancy rate from the Flights dataset accurately reflects passenger load.
- Ticket prices are stable within the quarter, per instructions.
- Delay costs are linear beyond the 15-minute grace period.
- Passenger behavior (baggage check rate) is consistent across routes.

## Known Limitations
- Ticket prices are based on sampled itinerary data, not full market coverage.
- Costs do not account for aircraft utilization differences beyond route assignment.
- No adjustment is made for directional imbalances or seasonality.

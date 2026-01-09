# Route Definition

## Definition
A route is defined as an **unordered airport pair** between two IATA airport codes.  
For example, JFK → ORD and ORD → JFK are treated as the same route.

## Why Unordered Pairs Are Required
The business decision is to invest in a **round-trip route served by a single dedicated aircraft**.  
Since revenue, cost, and utilization are evaluated at the round-trip level, treating each direction separately would double-count volume and distort profitability.

## Edge Cases Considered
- Directional imbalance (e.g., more demand one way than the other) is intentionally ignored at this stage, as the aircraft serves both legs of the route.
- Routes with flights in only one direction within the quarter are excluded from round-trip metrics.
- Airport pairs are normalized alphabetically to ensure consistent grouping.

## Impact on Metrics
- Busiest routes are counted using total round-trip flight volume, not individual legs.
- Profitability is calculated at the route level, aggregating costs and revenue across both directions.
- Breakeven analysis reflects the number of **round-trip cycles** required to recover the aircraft investment.

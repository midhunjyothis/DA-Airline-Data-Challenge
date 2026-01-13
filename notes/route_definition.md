# Route Definition

## Definition
A route is defined as an **unordered airport pair** between two IATA airport codes.  
For example, JFK–ORD and ORD–JFK are treated as the same route.

## Rationale
Each route represents a **round-trip investment served by a single dedicated aircraft**.  
Costs, revenue, and utilization are evaluated at the round-trip level, so treating directions separately would double-count volume and distort economics.

## Handling Edge Cases
- Directional imbalance is ignored at this stage.
- Routes with flights in only one direction during the quarter are excluded.
- Airport pairs are normalized alphabetically to ensure consistent grouping.

## Impact on Metrics
- Route volume is measured using round-trip counts, not individual flight legs.
- Profitability aggregates costs and revenue across both directions.
- Breakeven reflects the number of round-trip cycles required to recover the aircraft investment.

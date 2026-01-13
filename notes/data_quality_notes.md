## Flights Dataset

- `AIR_TIME` and `DISTANCE` are stored as object types despite representing numeric values. This matters because distance is used directly in mileage-based cost calculations.

- `DEP_DELAY` and `ARR_DELAY` contain a large number of missing values. Since delay minutes drive explicit cost rules, these gaps require deliberate handling.

- Cancelled flights are present and encoded as numeric flags. These rows align with many missing delay and air-time values and must be excluded to avoid inflating route counts and distorting cost and punctuality metrics.

- `OCCUPANCY_RATE` is missing for a small number of flights. The volume is limited, but occupancy is a primary revenue driver, so handling must be explicit.

- `TAIL_NUM` is missing for some records. While not required for route-level analysis, this indicates incomplete operational data and is noted for completeness.

## Tickets Dataset

- `ITIN_FARE` is stored as an object rather than numeric, preventing direct aggregation without type conversion.

- The `ROUNDTRIP` indicator is encoded as a float (1.0 / 0.0). Since the analysis considers round trips only, this column is a critical filter.

- `ITIN_FARE` and `PASSENGERS` both contain missing values. These records cannot reliably contribute to revenue calculations and are excluded.

- The dataset represents sampled ticket data rather than full coverage. Revenue estimates derived from it are directional rather than exact.

- Ticket records are itinerary-level, not flight-leg-level, creating a natural granularity mismatch with operational flight data.

## Airport Codes Dataset

- Most records are missing `IATA_CODE`, making them unusable for route matching with flight and ticket data.

- The dataset includes many non-relevant facility types (heliports, small airports, closed locations). Significant filtering is required to isolate medium and large airports.

- Several reference fields (`CONTINENT`, `MUNICIPALITY`, `ELEVATION_FT`) contain substantial missing values. These fields are not used directly and reinforce that this dataset serves as reference data only.

- Airport size is not directly labeled. Medium and large airport classification relies on provided metadata rather than inference from this dataset.

- This dataset is used only to determine route eligibility, not for operational or financial calculations.

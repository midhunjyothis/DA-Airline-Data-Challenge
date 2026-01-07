## Flights Dataset

- `AIR_TIME` and `DISTANCE` are stored as object types even though they represent numeric values. This is material because distance is used directly in mileage-based cost calculations.

- `DEP_DELAY` and `ARR_DELAY` contain a large number of missing values. Since delay minutes drive explicit operational cost rules, these gaps cannot be ignored and require a deliberate handling decision.

- Cancelled flights are present alongside completed flights and encoded as numeric flags. These rows align with many of the missing delay and air-time values and must be excluded early to avoid inflating route counts or distorting profitability and punctuality metrics.

- `OCCUPANCY_RATE` is missing for a small number of flights. The volume is limited, but occupancy is the primary driver of passenger revenue, so assumptions here must be made explicit rather than implicit.

- `TAIL_NUM` is missing for a subset of records. While tail numbers are not required for route-level analysis, the missingness indicates incomplete operational data and is noted for completeness.

## Tickets Dataset

- `ITIN_FARE` is stored as an object rather than a numeric type, which prevents direct aggregation of ticket revenue without explicit type handling.

- The `ROUNDTRIP` flag is encoded as a float (1.0 / 0.0). Since the analysis considers round trips only, this column becomes a critical filter and must be applied consistently.

- Both `ITIN_FARE` and `PASSENGERS` contain missing values. These records cannot reliably contribute to revenue calculations and require a clear exclusion or handling rule.

- The dataset represents a sample of ticket data rather than full coverage. Any revenue derived from it must be treated as an estimate rather than an exact measure.

- Ticket records are itinerary-level rather than flight-leg-level, creating a natural granularity mismatch when aligning with operational flight data.

## Airport Codes Dataset

- A large majority of records are missing `IATA_CODE`, which makes them unusable for matching routes in the Flights and Tickets datasets.

- The dataset includes many airport types such as heliports, small airports, and closed facilities. Since the analysis is restricted to medium and large airports, significant filtering is required.

- Several location-related fields (`CONTINENT`, `MUNICIPALITY`, `ELEVATION_FT`) contain substantial missing values. While not directly used in the analysis, this highlights that the dataset functions as reference data rather than a clean dimension table.

- Airport size is not explicitly labeled. Classification of medium and large airports must rely on provided metadata rather than assumptions from this dataset alone.

- This dataset is used only to determine route eligibility and not for any operational or financial calculations.

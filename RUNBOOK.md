# RUNBOOK

This document explains how to run, validate, and extend the airline route analysis.

---

## Data Expectations

The following files must exist under `data/`:
- Flights.csv
- Tickets.csv
- Airport_Codes.csv

Raw data is intentionally excluded from version control.

---

## Execution Order

The analysis is designed to be run in this order:

1. Load and validate raw data
2. Enrich flights with airport eligibility (medium / large only)
3. Aggregate flight activity to unordered route level
4. Aggregate ticket prices to route level
5. Compute route-level costs
6. Compute route-level revenue
7. Compute profitability and breakeven metrics
8. Produce tables and charts in the notebook

All of this is orchestrated inside `notebook.ipynb`.

---

## Code Design

- `src/` contains reusable, testable functions
- The notebook focuses on orchestration and interpretation
- Route is the primary grain (unordered airport pair)

This separation allows logic to be reused outside the notebook if needed.

---

## Development vs Final Cells

- Temporary sanity-check cells were used during development
- All validation-only cells were removed or commented out
- The final notebook is runnable end-to-end without manual intervention

---

## Known Limitations

- Ticket data is sampled and itinerary-based
- Revenue estimates are directional, not exact
- No seasonality or network optimization is modeled

These are intentional and documented.

---

## Extending the Work

To extend this project:
- Add additional quarters or years
- Replace sampled ticket data with full pricing
- Convert notebook logic into a scheduled pipeline
- Add monitoring around KPIs defined in `notes/`

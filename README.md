# Airline Data Challenge

This project analyzes which five US domestic round-trip routes an airline should invest in using 1Q2019 data.

Each route requires one dedicated aircraft with a $90M upfront cost.  
The airline’s brand promise is punctuality (“On time, for you”), so operational reliability is treated as a first-class decision factor.

The analysis answers the following:
- Top 10 busiest round-trip routes
- Top 10 most profitable round-trip routes (excluding aircraft purchase cost)
- 5 recommended routes to invest in
- Breakeven round trips for each recommended route
- KPIs to track route performance over time

Only the datasets provided in the challenge are used.

---

## Repository Structure

src/  
Reusable Python modules for loading data, aggregating routes, and calculating cost, revenue, and profit.

notes/  
Business reasoning, assumptions, tradeoffs, and limitations documented during the analysis.

metadata.md  
Definitions, units, and grain for all derived fields.

notebook.ipynb  
End-to-end analysis, tables, and visualizations used to answer the business questions.

RUNBOOK.md  
How to run the project and how the code is structured for reuse.

---

## How to Run

1. Create and activate a virtual environment  
2. Install dependencies:
   pip install -r requirements.txt

3. Place the following files under a local `data/` directory:
   - Flights.csv
   - Tickets.csv
   - Airport_Codes.csv

4. Run `notebook.ipynb` top to bottom

The notebook is designed to execute end-to-end without manual intervention.

---

## Key Notes

- Cancelled flights are excluded from all metrics
- Routes are defined as unordered airport pairs (round-trip level)
- Ticket data is sampled and treated as a pricing signal, not full revenue
- Occupancy is taken only from the Flights dataset, per instructions
- All metrics are based on 1Q2019 data only

---

## Outputs

All required tables, charts, and recommendations are produced in `notebook.ipynb`.  
Supporting assumptions and limitations are documented in `notes/` and `metadata.md`.

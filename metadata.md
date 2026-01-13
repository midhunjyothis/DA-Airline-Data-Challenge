# Derived Field Metadata

This document lists all derived fields created during the analysis.
The goal is clarity on definitions, units, and data grain so the work can be reused or audited.

All metrics are calculated using 1Q2019 data only.

---

## Route Definition Fields

### AIRPORT_A  
**Definition:** Alphabetically first airport IATA code in a route pair  
**Type:** String  
**Grain:** Route (unordered)  
**Why:** Ensures JFK–ORD and ORD–JFK are treated as the same round-trip route  

### AIRPORT_B  
**Definition:** Alphabetically second airport IATA code in a route pair  
**Type:** String  
**Grain:** Route (unordered)  
**Why:** Paired with AIRPORT_A to uniquely define a round-trip route  

---

## Volume & Activity Metrics

### flight_legs  
**Definition:** Total number of completed one-way flight legs for the route  
**Units:** Count  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Base activity measure used for cost and volume calculations  

### roundtrip_flights  
**Definition:** Number of completed round-trip flights (flight_legs / 2)  
**Units:** Count  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Core volume metric used for ranking routes and breakeven analysis  

---

## Distance & Cost Components

### total_distance  
**Definition:** Sum of flight distance across all completed legs on the route  
**Units:** Miles  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Drives mileage-based operating costs  

### total_distance_cost  
**Definition:** total_distance × $9.18 per mile  
**Units:** USD  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Represents fuel, maintenance, crew, depreciation, and insurance costs  

### total_airport_fees  
**Definition:** Sum of landing fees across all completed legs  
**Units:** USD  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Accounts for fixed operational costs at medium and large airports  

### total_delay_cost  
**Definition:** Delay minutes beyond the 15-minute grace period × $75  
**Units:** USD  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Quantifies cost impact of operational delays  

### total_cost  
**Definition:** Sum of distance cost, airport fees, and delay cost  
**Units:** USD  
**Grain:** Route (aggregated from flight-leg data)  
**Why:** Total modeled operating cost, excluding aircraft purchase  

---

## Revenue Components

### avg_roundtrip_fare  
**Definition:** Average round-trip ticket fare from sampled ticket data  
**Units:** USD  
**Grain:** Route (aggregated from ticket itinerary data)  
**Why:** Provides a route-level pricing signal for revenue estimation  

### avg_occupancy_rate  
**Definition:** Average seat occupancy rate from the Flights dataset  
**Units:** Proportion (0–1)  
**Grain:** Route (derived from aggregated flight-leg data)  
**Why:** Used to estimate passenger volume per flight  

### passengers_per_roundtrip  
**Definition:** avg_occupancy_rate × 200 seats  
**Units:** Passengers  
**Grain:** Route (derived from aggregated flight-leg data)  
**Why:** Converts occupancy into passenger counts  

### ticket_revenue_per_roundtrip  
**Definition:** avg_roundtrip_fare × passengers_per_roundtrip  
**Units:** USD  
**Grain:** Route (derived from route-level fare and occupancy)  
**Why:** Estimates fare-based revenue per round trip  

### baggage_revenue_per_roundtrip  
**Definition:** passengers_per_roundtrip × 50% × $70  
**Units:** USD  
**Grain:** Route (derived from route-level passenger estimate)  
**Why:** Models baggage fee revenue per round trip  

### total_revenue  
**Definition:** (ticket + baggage revenue per round trip) × roundtrip_flights  
**Units:** USD  
**Grain:** Route (derived from route-level revenue components)  
**Why:** Total modeled quarterly revenue  

---

## Profitability & Investment Metrics

### profit  
**Definition:** total_revenue − total_cost  
**Units:** USD  
**Grain:** Route  
**Why:** Primary profitability metric for route comparison  

### profit_per_roundtrip  
**Definition:** profit ÷ roundtrip_flights  
**Units:** USD  
**Grain:** Route  
**Why:** Normalizes profitability and supports breakeven analysis  

### breakeven_roundtrips  
**Definition:** $90,000,000 ÷ profit_per_roundtrip  
**Units:** Round trips  
**Grain:** Route  
**Why:** Measures how many round trips are required to recover aircraft investment  

---

## Notes
- Ticket prices are based on sampled itinerary data and treated as estimates.
- Occupancy is derived only from the Flights dataset, per instructions.
- Cancelled flights are excluded from all calculations.

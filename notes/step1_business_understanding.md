# Step 1 — Business Understanding

## Business Question
An airline plans to enter the US domestic market by launching **five round-trip routes** between **medium and large airports**.  
Each round-trip route requires **one dedicated aircraft**, with an **upfront cost of $90 million per aircraft**.

Using **1Q2019 flight, ticket, and airport data**, the objective is to determine which five round-trip routes the airline should invest in, given that the company’s brand promise is **“On time, for you.”**

## What Success Means
For this analysis, a successful route must satisfy **all three** conditions below:

1. **Profitable**  
   The route generates positive operating profit at the route level, excluding the upfront aircraft cost.

2. **Operationally Reliable**  
   The route demonstrates strong on-time performance and low disruption risk, consistent with a punctuality-focused brand.

3. **Sustainable in Volume**  
   The route shows consistent demand across the quarter, rather than being driven by short-term spikes or isolated anomalies.

## Key Tradeoffs Considered
This decision requires balancing several competing factors, none of which can be optimized in isolation:

- **Busiest vs. Most Profitable**  
  High-traffic routes may face congestion, delays, and competitive pressure that reduce reliability or margins.

- **Profitable vs. Punctual**  
  Some routes may appear profitable but consistently underperform on on-time metrics, creating brand risk.

- **Scale vs. Stability**  
  Routes with volatile demand or irregular operations may not be suitable for a dedicated aircraft.

## What This Analysis Does Not Over-Optimize
To stay focused and defensible, this analysis deliberately avoids:

- Optimizing for short-term or one-off revenue spikes  
- Modeling full airline network or fleet-sharing optimization  
- Adjusting for seasonality in ticket pricing (explicitly disallowed)  
- Using any data outside the datasets provided for this challenge  

## Hard Constraints From the Problem Statement
All downstream analysis strictly follows these rules:

- Only **1Q2019** data is used  
- Only **medium and large airports** are considered  
- **Cancelled flights are excluded** from route-level metrics  
- **Occupancy is derived only from the Flights dataset**  
- Each aircraft is **dedicated to a single round-trip route**  
- Punctuality is treated as a **core decision criterion**, not a secondary metric  

## Decision Framing
Each round-trip route is treated as an **independent $90M aircraft investment**.  
The final recommendation identifies **five routes** that best balance profitability, operational reliability, and sustainable demand under these constraints.

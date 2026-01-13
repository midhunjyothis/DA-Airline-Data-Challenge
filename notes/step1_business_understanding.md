# Step 1 : Business Understanding

## Business Question
An airline plans to enter the US domestic market by launching **five round-trip routes** between **medium and large airports**.  
Each route requires **one dedicated aircraft**, with an **upfront cost of $90M per aircraft**.

Using **1Q2019 flight, ticket, and airport data**, the goal is to decide which five routes to invest in, given a brand promise centered on punctuality (“On time, for you”).

## What Success Means
A route is considered successful if it meets all of the following:

- **Profitable**  
  Generates positive operating profit at the route level (excluding the upfront aircraft cost).

- **Operationally Reliable**  
  Shows reasonable on-time performance and manageable delay exposure.

- **Sustainable in Volume**  
  Supported by steady demand across the quarter, not driven by isolated spikes.

## Key Tradeoffs
No single metric is sufficient on its own. The analysis balances:

- **Busiest vs. Profitable**  
  High-volume routes can suffer from congestion, higher delay costs, and operational complexity.

- **Profit vs. Punctuality**  
  Some routes appear attractive financially but carry higher risk to on-time performance.

- **Scale vs. Stability**  
  Very low-volume routes may look profitable in aggregate but are less suitable for a dedicated aircraft.

## What Is Not Being Optimized
To keep the decision focused and defensible, the analysis does not attempt to:

- Chase short-term or one-off revenue spikes  
- Model full network effects or fleet sharing  
- Adjust ticket prices for seasonality (explicitly disallowed)  
- Use any data beyond what is provided in the challenge  

## Hard Constraints
All downstream analysis follows these rules:

- Only **1Q2019** data is used  
- Only **medium and large airports** are considered  
- **Cancelled flights are excluded**  
- **Occupancy comes only from the Flights dataset**  
- Each aircraft is **dedicated to one round-trip route**  
- Punctuality is treated as a **core decision factor**

## Decision Framing
Each route is evaluated as an independent **$90M aircraft investment**.  
The final output is a set of **five routes** that best balance profitability, reliability, and sustained demand under these constraints.

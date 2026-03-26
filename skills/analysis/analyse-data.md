# Analyse Data

**Category:** Analysis
**Tags:** data, CSV, statistics, interpretation, insights

## Description

Ask Claude to analyse a dataset (pasted as text or CSV) and surface key patterns, trends, and outliers. Useful for quick exploratory analysis without needing to write code.

## Prompt Template

```
Analyse the following dataset and provide:
1. A brief description of what the data represents.
2. Key statistics or trends (highs, lows, averages, notable patterns).
3. Any outliers or anomalies worth investigating.
4. 2–3 actionable insights or recommendations based on the data.

Dataset:
[PASTE DATA HERE — CSV, table, or plain list]
```

## Example

**Input:**
> Analyse the following dataset...
>
> ```
> Month, Revenue ($), Customers
> Jan, 42000, 310
> Feb, 39000, 290
> Mar, 51000, 375
> Apr, 53000, 390
> May, 48000, 350
> Jun, 61000, 430
> ```

**Output:**
> **1. Description:** Monthly revenue and customer counts for a six-month period (Jan–Jun).
>
> **2. Key trends:**
> - Revenue grew from $42k in January to $61k in June — a 45% increase over six months.
> - Customer count tracked closely with revenue, suggesting revenue per customer is relatively stable (~$135–$142 per customer each month).
> - February was the only month with a decline; both revenue and customers dropped from January levels.
>
> **3. Anomalies:**
> - The February dip (−7% revenue, −6% customers) is worth investigating — it may reflect seasonal patterns or a specific campaign that ended.
>
> **4. Insights:**
> - The strong correlation between customers and revenue suggests that customer acquisition is the primary growth lever — prioritise acquisition over upsell in the short term.
> - The June jump (+27% vs May) is the largest month-on-month increase; understanding what drove it could help replicate the result.
> - If February dips are seasonal, plan marketing campaigns or promotions in advance to counteract the trend next year.

## Notes

- For larger datasets, paste a representative sample and ask Claude to focus on specific columns or questions.
- You can ask for a specific output format: "Present findings as a bulleted executive summary" or "Format as a table".
- Follow up with the [Reasoning — Pros and Cons](../reasoning/pros-and-cons.md) skill to evaluate options surfaced by the analysis.

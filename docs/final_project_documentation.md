# Final Project Documentation

## 1. Project Overview

`Uber_Analysis` is a complete ride-hailing analytics capstone built around a 50,000-row Uber trips dataset covering six U.S. cities. The project combines data cleaning, feature engineering, exploratory analysis, statistical validation, and Tableau dashboard design to document how demand, revenue, and service outcomes vary across the operating footprint.

Unlike the `SuperStore_Analysis` project, this Uber project is documented and delivered through a single final BI platform:

- Tableau Public

The supporting work in Python and Jupyter exists to validate the business story, prepare the Tableau-ready dataset, and keep the analysis reproducible.

## 2. Project Objectives

The project was designed to answer the following business questions:

1. How reliable is trip fulfillment across the six-city footprint?
2. Which cities and time windows contribute the most revenue and trip demand?
3. How balanced or imbalanced are rider, driver, payment, and fare-tier patterns?
4. Are the differences across cities and segments operationally meaningful, or mainly useful for monitoring?

## 3. Dataset Summary

| Item | Value |
|---|---|
| Source | Kaggle Uber Trips dataset |
| Raw rows | 50,000 |
| Final cleaned rows | 49,997 |
| Raw columns | 14 |
| Cleaned columns | 23 |
| Tableau-ready columns | 17 |
| Coverage | 2023-01-01 00:00:00 to 2023-02-04 17:19:00 |
| Unique pickup dates | 35 |
| Cities | Boston, Chicago, Los Angeles, New York, San Francisco, Seattle |
| Unique drivers | 8,963 |
| Unique riders | 38,351 |
| Dataset authenticity | Synthetic sample trip data rather than verified real Uber operational records |
| Known limitation | Coordinates are synthetic and unsuitable for geographic analysis |

## 4. Data Workflow

### Extraction and Validation Layer

The raw dataset was first inspected for:

- schema consistency
- null values
- duplicate rows
- duplicate trip identifiers
- datetime coverage

The raw extract passed the missing-value and duplicate checks, but a later duration review identified a small set of invalid ghost trips.

### Cleaning and Feature Engineering Layer

The cleaning workflow completed the following steps:

- converted `pickup_time` and `drop_time` to datetime
- standardized `city`, `status`, and `payment_method`
- removed 3 ghost trips with zero distance and zero duration
- created 9 derived analysis fields

The cleaned dataset is the master analytical dataset used for notebook analysis and KPI validation.

### Tableau Preparation Layer

The Tableau export keeps only the 17 fields needed for:

- KPI cards
- page filters
- time-series charts
- city comparisons
- operational and business-performance views

This final export also adds `day_type` and `fare_tier` so the dashboard can use business-friendly segmentation without extra workbook logic.

## 5. Dataset Authenticity Note

The source used in this project should be treated as synthetic sample trip data rather than as verified real Uber operational records. That matters for interpretation:

- the dashboard structure and workflow are valid portfolio deliverables
- the KPI logic and analytical process remain useful
- the findings should not be presented as audited conclusions about actual Uber business performance

## 6. Validated KPI Baseline

The following KPI baseline uses `data/processed/uber_cleaned_dataset.csv`.

| KPI | Value |
|---|---|
| Total Trips | 49,997 |
| Total Revenue | $798,800.27 |
| Average Fare | $15.98 |
| Average Distance | 7.01 km |
| Average Trip Duration | 21.03 minutes |
| Completed Trips | 42,538 |
| Completion Rate | 85.08% |
| Cancelled Trips | 4,984 |
| Cancellation Rate | 9.97% |
| No-Show Trips | 2,475 |
| No-Show Rate | 4.95% |

## 7. Business Findings

### Service Outcomes

- The operating model is largely stable, with 85.08% of trips completed.
- Cancellations are the main reliability issue, occurring nearly twice as often as no-shows.
- Boston shows the highest cancellation rate at 10.33%.
- Los Angeles shows the highest no-show rate at 5.24%.
- San Francisco has the lowest cancellation rate at 9.65%.

Key conclusion:

The dashboard should treat cancellations as the leading operational exception and no-shows as the secondary risk to monitor by city.

### Revenue and City Performance

| City | Trips | Revenue | Average Fare |
|---|---|---|---|
| Boston | 8,454 | $135,704.41 | $16.05 |
| San Francisco | 8,401 | $134,611.24 | $16.02 |
| Chicago | 8,344 | $132,689.49 | $15.90 |
| New York | 8,247 | $132,351.73 | $16.05 |
| Seattle | 8,236 | $132,287.32 | $16.06 |
| Los Angeles | 8,315 | $131,156.08 | $15.77 |

Key conclusion:

Revenue is balanced across the six cities. Boston leads, but no city dominates the dataset strongly enough to justify a single-market narrative.

### Time and Demand Patterns

- `Night (0-6)` has the highest trip count at 12,600 trips.
- `Morning (6-12)` produces the highest revenue at $202,099.41.
- `Night (0-6)` is a close second in revenue at $200,670.16.
- Weekdays contribute $576,090.41 in revenue, compared with $222,709.86 on weekends.

Key conclusion:

The most valuable monitoring windows are weekday demand overall and the `Morning (6-12)` plus `Night (0-6)` time segments.

### Pricing and Customer Behaviour

- Payment-method usage is extremely balanced across UPI, Card, Wallet, and Cash.
- Premium fare-tier trips contribute $383,376.89 in revenue, the largest share among the three fare tiers.
- Fare has a strong correlation of 0.871 with both trip distance and trip duration.

Key conclusion:

The pricing model appears internally consistent, and the dashboard should emphasize mix monitoring rather than pricing anomalies as the primary story.

### Statistical Context

- Weekday and weekend fares do not differ meaningfully in practice (`p = 0.1366`).
- Fare differences across cities are statistically detectable but practically trivial (`eta squared = 0.000284`).
- The association between city and status is negligible (`Cramer's V = 0.0083`).

Key conclusion:

The Uber dashboard is strongest as a descriptive monitoring tool. The evidence does not support exaggerated claims that one city or segment behaves fundamentally differently from the others.

## 8. Dashboard Deliverables

| Deliverable | Role |
|---|---|
| Tableau Public dashboard | Final interactive analysis and presentation layer |
| Tableau workbook | Editable project source |
| Screenshots archive | Static project documentation and portfolio backup |

The Tableau dashboard pages are:

1. `Overview`
2. `Business Insights`
3. `Operations`

## 9. Final Recommendations

1. Track cancellation rate as the primary service-quality KPI, with special attention to Boston and Los Angeles.
2. Monitor `Morning (6-12)` and `Night (0-6)` as the most valuable demand windows for operational staffing and supply planning.
3. Use the city comparison charts to flag exceptions, but avoid overinterpreting small city-level differences as structural market gaps.
4. Keep payment and fare-tier mix visible because these are stable segmentation views that support ongoing monitoring without relying on synthetic geography.
5. Preserve the Tableau-ready export structure so the workbook remains lean, reproducible, and easy to refresh.

## 10. Documentation Scope Note

This document is the formal project-level documentation for `Uber_Analysis`.

It is broader than the Tableau-specific dashboard guide in:

- [../tableau/tableau_dashboard_guide.md](../tableau/tableau_dashboard_guide.md)

The Tableau guide focuses on page structure, filters, calculations, and dashboard assets. This project document covers the full analytical workflow and business narrative.

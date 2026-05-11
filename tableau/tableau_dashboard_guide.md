# Tableau Dashboard Guide - Uber Analysis

This guide documents the finished Tableau Public dashboard for `Uber_Analysis`. It explains the workbook structure, dataset inputs, filters, key calculations, and the purpose of each page in the published dashboard.

## 1. Dashboard Goal

The Tableau workbook is the final presentation layer of the project. Its role is to help viewers monitor:

- trip volume
- revenue performance
- service outcomes
- fare mix
- rider and driver activity
- operational differences across cities and time windows

The supporting statistical analysis shows that the dataset is relatively balanced across cities, so the dashboard is intentionally designed for descriptive monitoring rather than exaggerated causal storytelling.

## 2. Dataset Used in Tableau

The workbook uses:

`Uber_Analysis/data/processed/tableau_ready_dataset.csv`

The file contains:

- 49,997 rows
- 17 columns
- one row per trip

The final Tableau fields are:

`trip_id`, `driver_id`, `rider_id`, `city`, `distance_km`, `fare_amount`, `status`, `payment_method`, `pickup_time`, `pickup_date`, `pickup_hour`, `pickup_day`, `time_of_day`, `trip_duration_mins`, `fare_per_km`, `day_type`, `fare_tier`

## 3. Published Dashboard Pages

The final workbook is organized into three pages.

### Overview

Primary purpose:

- provide the headline KPI summary and the first-pass operational picture

Main components:

- `Total Trips`
- `Total Revenue`
- `Complete %`
- `Avg Fare`
- `Daily Trip Trend`
- `Trip Status Mix`
- `Trips by City`

### Business Insights

Primary purpose:

- show how revenue, fare mix, and customer activity are distributed

Main components:

- `Riders`
- `Rev / Driver`
- `Revenue by City`
- `Average Fare by City`
- `Fare Distribution by Tier`
- `Revenue by Day Type`
- `Revenue by Time of Day`
- `Revenue by Fare Tier`

### Operations

Primary purpose:

- focus on reliability and operating health

Main components:

- `Drivers`
- `Riders`
- `Cancellation Rate by City`
- `No-Show Rate by City`
- `Trips by Time of Day`
- `Payment Method Mix`

## 4. Shared Filters

The dashboard uses the same shared filters across pages:

- `city`
- `pickup_date`
- `status`
- `payment_method`
- `time_of_day`
- `day_type`
- `fare_tier`

Recommended display types in the workbook:

- `city`: Multiple Values Dropdown
- `pickup_date`: Range of Dates
- `status`: Multiple Values Dropdown
- `payment_method`: Multiple Values Dropdown
- `time_of_day`: Multiple Values Dropdown
- `day_type`: Dropdown
- `fare_tier`: Multiple Values Dropdown

## 5. Core Calculated Fields

The finished workbook relies on these core calculations:

`Total Trips`

```tableau
COUNT([trip_id])
```

`Active Drivers`

```tableau
COUNTD([driver_id])
```

`Active Riders`

```tableau
COUNTD([rider_id])
```

`Completed Trips`

```tableau
SUM(IIF([status] = 'Completed', 1, 0))
```

`Cancelled Trips`

```tableau
SUM(IIF([status] = 'Cancelled', 1, 0))
```

`No-Show Trips`

```tableau
SUM(IIF([status] = 'No-Show', 1, 0))
```

`Complete %`

```tableau
SUM(IIF([status] = 'Completed', 1, 0)) / COUNT([trip_id])
```

`Cancellation Rate`

```tableau
SUM(IIF([status] = 'Cancelled', 1, 0)) / COUNT([trip_id])
```

`No-Show Rate`

```tableau
SUM(IIF([status] = 'No-Show', 1, 0)) / COUNT([trip_id])
```

`Total Revenue`

```tableau
SUM([fare_amount])
```

`Avg Fare`

```tableau
AVG([fare_amount])
```

`Rev / Driver`

```tableau
SUM([fare_amount]) / COUNTD([driver_id])
```

## 6. Visual Design Notes

The final workbook follows an Uber-inspired neutral design language:

- black header bar
- white and light-grey dashboard background
- black and grey marks with restrained categorical contrast
- simple, business-style typography
- minimal decorative elements so the dashboard stays presentation-ready

This design choice keeps the focus on KPIs, comparisons, and filters rather than on decorative styling.

## 7. Dashboard Assets

| Asset | Path |
|---|---|
| Workbook | [workbook/Uber Trips Analysis.twbx](./workbook/Uber%20Trips%20Analysis.twbx) |
| Overview screenshot | [screenshots/overview.png](./screenshots/overview.png) |
| Business Insights screenshot | [screenshots/business_insights.png](./screenshots/business_insights.png) |
| Operations screenshot | [screenshots/operations.png](./screenshots/operations.png) |
| Published link index | [dashboard_links.md](./dashboard_links.md) |

## 8. Dashboard Interpretation Notes

- The city charts are intentionally comparative, but the metric spread is narrow across cities.
- Time-of-day views are more decision-relevant than city differences for this dataset.
- Service-outcome views are essential because cancellation is the main operational exception.
- Synthetic coordinates are excluded, so the dashboard avoids maps and keeps the analysis focused on reliable business dimensions.

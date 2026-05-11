# Data Dictionary - Uber Trips Project

This document defines the raw fields, cleaned analytical fields, and final Tableau-ready fields used in `Uber_Analysis`.

## Dataset Summary

| Item | Details |
|---|---|
| Raw dataset | `data/raw/uber_raw_dataset.csv` |
| Cleaned dataset | `data/processed/uber_cleaned_dataset.csv` |
| Tableau-ready dataset | `data/processed/tableau_ready_dataset.csv` |
| Grain | One row per trip |
| Date coverage | 2023-01-01 00:00:00 to 2023-02-04 17:19:00 |
| Unique pickup dates | 35 |
| Raw rows / columns | 50,000 / 14 |
| Cleaned rows / columns | 49,997 / 23 |
| Tableau-ready rows / columns | 49,997 / 17 |
| Cities | Boston, Chicago, Los Angeles, New York, San Francisco, Seattle |
| Dataset authenticity | Synthetic sample trip data |
| Dashboard limitation | Coordinates are synthetic and excluded from Tableau |

## Raw Columns

| Column | Type | Description | Example | Notes |
|---|---|---|---|---|
| `trip_id` | int | Unique trip identifier | `1` | Primary counting field for trip-level KPIs |
| `driver_id` | int | Driver identifier | `8270` | Used for active-driver counts |
| `rider_id` | int | Rider identifier | `10683` | Used for rider counts |
| `city` | string | Trip origin city | `San Francisco` | Standardized during cleaning |
| `pickup_lat` | float | Pickup latitude | `37.1709` | Retained in cleaned data only |
| `pickup_lng` | float | Pickup longitude | `-77.5865` | Retained in cleaned data only |
| `drop_lat` | float | Drop latitude | `37.1737` | Retained in cleaned data only |
| `drop_lng` | float | Drop longitude | `-77.6199` | Retained in cleaned data only |
| `distance_km` | float | Trip distance in kilometres | `2.97` | Core demand and pricing metric |
| `fare_amount` | float | Trip fare amount | `10.71` | Core revenue metric |
| `status` | string | Trip outcome | `Completed` | Values standardized to `Completed`, `Cancelled`, `No-Show` |
| `payment_method` | string | Rider payment method | `Wallet` | Values standardized to `Cash`, `Card`, `UPI`, `Wallet` |
| `pickup_time` | string in raw file | Pickup timestamp | `2023-01-01 00:00:00` | Converted to datetime during cleaning |
| `drop_time` | string in raw file | Drop timestamp | `2023-01-01 00:08:54.600000000` | Converted to datetime during cleaning |

## Derived Columns in the Cleaned Dataset

These 9 fields are added during notebook-based cleaning and feature engineering.

| Column | Type | Logic | Business Use |
|---|---|---|---|
| `trip_duration_mins` | float | `(drop_time - pickup_time)` in minutes, rounded to 2 decimals | Service-time and operations analysis |
| `pickup_date` | date | Date extracted from `pickup_time` | Daily trend analysis and filters |
| `pickup_hour` | int | Hour extracted from `pickup_time` | Hourly demand profiling |
| `pickup_day` | string | Day name derived from `pickup_time` | Weekday pattern analysis |
| `pickup_month` | string | Month name derived from `pickup_time` | Retained for analysis completeness |
| `pickup_week` | int | ISO week number derived from `pickup_time` | Retained for week-level grouping |
| `time_of_day` | string | Bucketed from `pickup_hour` | User-friendly time segmentation |
| `fare_per_km` | float | `fare_amount / distance_km` where distance is non-zero | Pricing-efficiency analysis |
| `is_weekend` | bool | `True` when pickup falls on Saturday or Sunday | Intermediate day-type logic |

## Tableau-Specific Derived Fields

These fields are added during final Tableau preparation, not during the original cleaning step.

| Column | Type | Logic | Business Use |
|---|---|---|---|
| `day_type` | string | Converts `is_weekend` to readable labels `Weekday` and `Weekend` | Dashboard slicing and weekday-weekend comparison |
| `fare_tier` | string | Tercile-based segmentation of `fare_amount` using cutoffs near `12.92` and `18.21` | Revenue mix and pricing segmentation |

## Final Tableau-Ready Columns

The Tableau export is intentionally lean and keeps only the columns required for the published dashboard.

| Column | Type in CSV | Description |
|---|---|---|
| `trip_id` | int | Trip-level counting field |
| `driver_id` | int | Active-driver counting field |
| `rider_id` | int | Active-rider counting field |
| `city` | string | Primary city segmentation field |
| `distance_km` | float | Distance metric |
| `fare_amount` | float | Revenue metric |
| `status` | string | Service-outcome filter and KPI input |
| `payment_method` | string | Payment segmentation |
| `pickup_time` | datetime-like string | Timestamp for continuous time analysis |
| `pickup_date` | date-like string | Daily trend and date filter field |
| `pickup_hour` | int | Hour-based drill-down field |
| `pickup_day` | string | Day-of-week analysis field |
| `time_of_day` | string | Bucketed time segment used in charts and filters |
| `trip_duration_mins` | float | Duration KPI |
| `fare_per_km` | float | Pricing-efficiency KPI |
| `day_type` | string | Readable weekday-weekend label |
| `fare_tier` | string | Budget, Standard, and Premium fare segment |

## Columns Excluded from the Tableau Export

| Column | Why It Was Excluded |
|---|---|
| `pickup_lat`, `pickup_lng`, `drop_lat`, `drop_lng` | Coordinates are synthetic and not appropriate for mapping |
| `drop_time` | `trip_duration_mins` already captures the useful operational timing outcome |
| `pickup_month`, `pickup_week` | Can be derived or are not required for the final dashboard story |
| `is_weekend` | Replaced by the more readable `day_type` field |

## Data Quality Notes

- No missing values were found in the raw dataset.
- No duplicate rows or duplicate `trip_id` values were found.
- Three ghost trips with zero distance and zero duration were removed during cleaning.
- Fare, distance, and duration are internally consistent enough for descriptive analysis and dashboarding.
- Tableau intentionally excludes the GPS coordinates because the source coordinates are synthetic rather than real trip geography.

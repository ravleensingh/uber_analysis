# Data Dictionary -- Uber Trips Dataset

This document provides a complete reference for every column in the Uber trips dataset, covering both the original raw fields and the derived columns created during the cleaning pipeline.

---

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Uber Trips Dataset (50K) |
| Source | Kaggle (raw transactional trip records) |
| Raw file name | `uber_trips_dataset_50k.csv` |
| Cleaned file name | `uber_trips_cleaned.csv` |
| Granularity | One row per trip |
| Time period | January 2023 (full month) |
| Raw row count | 50,000 |
| Clean row count | 49,997 |
| Raw column count | 14 |
| Final column count | 23 (14 original + 9 derived) |

---

## Original Columns (from raw dataset)

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `trip_id` | int | Unique identifier for each trip | 1 | Deduplication | No changes required; all values unique |
| `driver_id` | int | Identifier for the driver assigned to the trip | 8270 | Segmentation | No changes required |
| `rider_id` | int | Identifier for the rider who requested the trip | 10683 | Segmentation | No changes required |
| `city` | category | City where the trip originated | San Francisco | EDA, KPI, Tableau filters | Stripped whitespace, applied title case, converted to category dtype |
| `pickup_lat` | float | Latitude of the pickup location | 37.1709 | Geographic analysis | No changes required |
| `pickup_lng` | float | Longitude of the pickup location | -77.5865 | Geographic analysis | No changes required |
| `drop_lat` | float | Latitude of the drop-off location | 37.1737 | Geographic analysis | No changes required |
| `drop_lng` | float | Longitude of the drop-off location | -77.6199 | Geographic analysis | No changes required |
| `distance_km` | float | Distance covered during the trip in kilometres | 2.97 | EDA, KPI, Tableau | No changes required; validated no negatives |
| `fare_amount` | float | Amount charged for the trip (in currency units) | 10.71 | EDA, KPI, Tableau | Validated no negatives |
| `status` | category | Trip outcome | Completed | EDA, KPI, Tableau filters | Stripped whitespace, applied title case, converted to category dtype. Values: Completed, Cancelled, No-Show |
| `payment_method` | category | Payment method used by the rider | Wallet | EDA, KPI, Tableau filters | Stripped whitespace, applied title case, converted to category dtype. Values: Cash, Card, Upi, Wallet |
| `pickup_time` | datetime64 | Timestamp when the trip started | 2023-01-01 00:00:00 | Temporal analysis, feature engineering | Converted from string to datetime64 |
| `drop_time` | datetime64 | Timestamp when the trip ended | 2023-01-01 00:08:54 | Temporal analysis, feature engineering | Converted from string to datetime64 |

---

## Derived Columns (created during cleaning)

| Derived Column | Data Type | Logic | Business Meaning |
|---|---|---|---|
| `trip_duration_mins` | float | `(drop_time - pickup_time)` converted to minutes, rounded to 2 decimal places | Core metric for service quality and operational efficiency analysis |
| `pickup_date` | date | Date portion extracted from `pickup_time` | Enables day-level trend analysis and aggregation |
| `pickup_hour` | int | Hour (0-23) extracted from `pickup_time` | Identifies peak and off-peak demand hours |
| `pickup_day` | string | Day-of-week name (e.g., Monday) extracted from `pickup_time` | Supports weekday pattern analysis and scheduling decisions |
| `pickup_month` | string | Month name (e.g., January) extracted from `pickup_time` | Enables monthly trend comparison (single month in this dataset) |
| `pickup_week` | int | ISO week number extracted from `pickup_time` | Supports weekly aggregation and trend analysis |
| `time_of_day` | string | Hour bucketed into segments: Night (0-6), Morning (6-12), Afternoon (12-17), Evening (17-21), Night (21-24) | Human-readable time segment for dashboard filters and demand pattern analysis |
| `fare_per_km` | float | `fare_amount / distance_km` (NaN where distance is zero) | Measures pricing efficiency per trip; useful for identifying pricing anomalies |
| `is_weekend` | bool | True if the trip fell on Saturday or Sunday | Quick filter for weekend versus weekday demand comparison |

---

## Data Quality Notes

- **No missing values** were found in the raw dataset across any column.
- **No duplicate rows** or duplicate `trip_id` values were found.
- **3 ghost trips** (zero distance and zero duration with non-zero fare) were identified and removed during cleaning.
- **GPS coordinates** appear to have some geographic inconsistency (e.g., coordinates for "Boston" may not match actual Boston geography). This is a known limitation of the synthetic dataset and does not affect the analytical value of other columns.
- **Fare currency** is not explicitly labelled in the raw data. Values are treated as unitless numerical amounts for analysis.
- **Single-month coverage**: the dataset covers January 2023 only, which limits seasonal or multi-month trend analysis.

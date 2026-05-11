# Uber Trips Dataset - Data Cleaning Report

**Project:** Uber Ride-Hailing Operations and Revenue Analysis  
**Stage:** Data Cleaning and Transformation  
**Raw Input:** `data/raw/uber_raw_dataset.csv`  
**Cleaned Output:** `data/processed/uber_cleaned_dataset.csv`  
**Final Tableau Output:** `data/processed/tableau_ready_dataset.csv`  
**Records:** 50,000 raw rows to 49,997 cleaned and Tableau-ready rows

## Purpose

This report documents the cleaning logic used to prepare the Uber trips dataset for exploratory analysis, statistical review, and Tableau dashboard development.

## Dataset Authenticity Note

The project documentation treats this source as synthetic sample trip data rather than as verified real Uber operational trip history. The data is suitable for demonstrating cleaning, feature engineering, dashboard design, and KPI analysis, but the findings should not be framed as audited conclusions about actual Uber operations.

## 1. Raw Dataset Review

The raw dataset contains 50,000 trip-level records and 14 source columns. Each row represents a single trip and includes:

- trip, driver, and rider identifiers
- city
- synthetic pickup and drop coordinates
- distance and fare
- trip status
- payment method
- pickup and drop timestamps

Initial validation showed:

- no missing values
- no duplicate rows
- no duplicate `trip_id` values
- pickup coverage from `2023-01-01 00:00:00` to `2023-02-04 17:19:00`

## 2. Data Type Corrections

The following type corrections were applied during cleaning:

- `pickup_time` converted from string to datetime
- `drop_time` converted from string to datetime
- `city`, `status`, and `payment_method` standardized as categorical business fields

These conversions were required for consistent time-based feature engineering and reliable categorical analysis.

## 3. Text Standardization

Three categorical fields were standardized:

- `city`
- `status`
- `payment_method`

Cleaning rules applied:

- removed leading and trailing whitespace
- normalized case and spelling consistency
- standardized payment methods to `Cash`, `Card`, `UPI`, and `Wallet`

## 4. Anomaly Detection and Row Removal

After datetime conversion, trip duration was calculated from pickup and drop timestamps. This surfaced 3 ghost trips where:

- `distance_km = 0`
- `trip_duration_mins = 0`
- a non-zero fare still appeared

These rows were treated as invalid operational events and removed from the final cleaned dataset.

## 5. Derived Columns Added

Nine analytical fields were added during cleaning:

| Column | Purpose |
|---|---|
| `trip_duration_mins` | Service-time measurement |
| `pickup_date` | Daily aggregation and filtering |
| `pickup_hour` | Hourly demand analysis |
| `pickup_day` | Day-of-week analysis |
| `pickup_month` | Month-level grouping if required |
| `pickup_week` | Week-level grouping if required |
| `time_of_day` | User-friendly time segmentation |
| `fare_per_km` | Pricing-efficiency metric |
| `is_weekend` | Weekend versus weekday comparison |

## 6. Final Validation Checks

The cleaned dataset passed the following checks:

| Validation | Result |
|---|---|
| Missing values remaining | 0 |
| Duplicate rows remaining | 0 |
| Duplicate `trip_id` values remaining | 0 |
| Negative fares | 0 |
| Negative distances | 0 |
| Negative durations | 0 |
| Drop time earlier than pickup time | 0 |

## 7. Final Cleaned Dataset Summary

| Metric | Value |
|---|---|
| Rows | 49,997 |
| Columns | 23 |
| Cities | 6 |
| Drivers | 8,963 |
| Riders | 38,351 |
| Date range | 2023-01-01 to 2023-02-04 |
| Total revenue | $798,800.27 |
| Average fare | $15.98 |
| Average distance | 7.01 km |
| Average duration | 21.03 minutes |

## 8. Tableau Preparation Notes

The final Tableau export keeps the same 49,997 validated rows but reduces the schema from 23 columns to 17 business-facing fields.

The Tableau-specific preparation also:

- converts `is_weekend` into the readable `day_type` field
- adds `fare_tier` to support pricing segmentation
- excludes synthetic coordinate fields from dashboard use
- removes fields that are unnecessary for the final published visuals

## 9. Cleaning Conclusion

The dataset is analytically clean, internally consistent, and well suited for descriptive dashboarding. The primary data caveat is not row quality but source realism: the coordinate fields are synthetic, so the project intentionally avoids geographic mapping and focuses instead on operational, revenue, and service-outcome analysis.

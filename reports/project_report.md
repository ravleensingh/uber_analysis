# Project Report: Uber Ride-Hailing Analysis Dashboard Portfolio

## 1. Executive Summary

This project analyzes a 50,000-row Uber trips dataset to understand service reliability, revenue distribution, rider behavior, and operational performance across six U.S. cities. The work uses Python and Jupyter for cleaning, exploratory analysis, and validation, then delivers the final business story through a three-page Tableau Public dashboard.

After cleaning, the final analytical dataset contains 49,997 trip records and 23 columns. A lean 17-column export was then prepared for Tableau. Across the final cleaned dataset, the project records 49,997 trips, $798,800.27 in revenue, an average fare of $15.98, and an overall completion rate of 85.08%.

The core result is that the operating footprint is relatively balanced across cities. The dashboard is most valuable as a monitoring tool for service outcomes, time-of-day demand, fare-tier mix, and city-level exceptions rather than as evidence of large structural gaps between markets.

## 2. Project Objective

The objective of the project was to answer four business questions:

1. How reliable is trip completion across the available markets?
2. Which cities, day types, and time windows drive the most demand and revenue?
3. How do fare mix, rider counts, driver activity, and payment behavior support operational monitoring?
4. Which observed differences are business-relevant, and which are statistically small despite large sample sizes?

## 3. Data Foundation

### Source and Scope

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
| Cities covered | 6 |
| Unique drivers | 8,963 |
| Unique riders | 38,351 |
| Dataset authenticity | Synthetic sample trip data rather than verified real Uber trip operations |

### Data Quality and Cleaning

- No missing values were found in the raw extract.
- No duplicate rows or duplicate `trip_id` values were found.
- Three ghost trips were removed because they showed zero distance and zero duration.
- The cleaned dataset preserves the original 14 source fields and adds 9 engineered analytical fields.
- The final Tableau export keeps only the 17 fields required for dashboarding and adds `day_type` plus `fare_tier`.

### Authenticity Note

The dataset should be treated as synthetic sample trip data rather than as verified real Uber operational history. That means the project is strongest as a dashboarding, analytics, and documentation portfolio piece, while the final findings should be framed as insights from sample data rather than as audited conclusions about the real company.

## 4. Workflow

| Layer | Purpose | Main Outputs |
|---|---|---|
| Extraction | Inspect schema, duplicates, nulls, and date coverage | `01_extraction.ipynb` |
| Cleaning | Standardize text, convert datetime fields, remove ghost trips, engineer features | `02_cleaning.ipynb`, `uber_cleaned_dataset.csv` |
| EDA | Profile demand, revenue, city performance, and service-outcome patterns | `03_eda.ipynb` |
| Statistical analysis | Validate correlations and test whether visible differences are meaningful | `04_statistical_analysis.ipynb` |
| Tableau prep | Export the lean dashboard dataset and reconcile final KPIs | `05_final_load_prep.ipynb`, `tableau_ready_dataset.csv` |

## 5. KPI Baseline

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

## 6. Findings

### 6.1 Service Reliability

- Completed trips dominate the dataset at 85.08%.
- Cancelled trips account for 9.97%.
- No-show trips account for 4.95%.
- Boston has the highest cancellation rate at 10.33%.
- Los Angeles has the highest no-show rate at 5.24%.
- San Francisco has the lowest cancellation rate at 9.65%.

Interpretation:

The operating system is broadly reliable, but the main failure mode is cancellation rather than rider no-show. Operational review should start with cancellation patterns first.

### 6.2 Revenue and City Performance

| City | Trips | Revenue | Average Fare | Revenue per Driver |
|---|---|---|---|---|
| Boston | 8,454 | $135,704.41 | $16.05 | $24.88 |
| San Francisco | 8,401 | $134,611.24 | $16.02 | $24.55 |
| Chicago | 8,344 | $132,689.49 | $15.90 | $24.38 |
| New York | 8,247 | $132,351.73 | $16.05 | $24.63 |
| Seattle | 8,236 | $132,287.32 | $16.06 | $24.78 |
| Los Angeles | 8,315 | $131,156.08 | $15.77 | $23.79 |

Interpretation:

- Boston leads the dataset on both trips and revenue.
- Los Angeles is lowest on revenue and revenue per driver.
- The spread across cities is narrow, which supports a balanced-market interpretation rather than a winner-versus-laggard story.

### 6.3 Time-of-Day and Day-Type Patterns

- `Night (0-6)` contains the highest trip count at 12,600 trips.
- `Morning (6-12)` is the strongest revenue window at $202,099.41.
- `Night (0-6)` is a close second at $200,670.16.
- Weekdays contribute 72% of trips and $576,090.41 in revenue.
- Weekends contribute 28% of trips and $222,709.86 in revenue.

Interpretation:

Time segmentation matters more than city segmentation in this dataset. The dashboard should keep staffing and demand monitoring centered on weekday flow, early-day volume, and overnight demand.

### 6.4 Customer, Payment, and Fare Mix

- The project contains 38,351 unique riders and 8,963 unique drivers.
- Payment-method counts are nearly even, led by UPI at 12,548 and Card at 12,531, with Wallet at 12,505 and Cash at 12,413.
- Premium fare-tier revenue is $383,376.89.
- Standard fare-tier revenue is $258,378.27.
- Budget fare-tier revenue is $157,045.11.

Interpretation:

There is no dominant payment method or rider-type imbalance. Fare tier is the clearer business segmentation, with Premium contributing the largest share of revenue.

### 6.5 Statistical Validation

- Fare correlates strongly with distance (`0.871`) and duration (`0.871`).
- Weekday versus weekend fare difference is not statistically significant at conventional thresholds (`p = 0.1366`).
- The effect size for weekday versus weekend fare difference is trivial (`Cohen's d = 0.0148`).
- Fare differences across cities are statistically detectable (`p = 0.0145`) but practically tiny (`eta squared = 0.000284`).
- The relationship between city and trip status is negligible (`Cramer's V = 0.0083`).

Interpretation:

The statistical analysis reinforces the dashboard strategy: use the visuals for operational monitoring, descriptive segmentation, and exception tracking rather than strong causal storytelling.

## 7. Dashboard Design Implications

The final Tableau workbook is structured as three coordinated pages:

1. `Overview`
   Focuses on headline KPIs, daily trip trend, trip-status mix, and city trip volume.
2. `Business Insights`
   Focuses on riders, revenue per driver, fare-tier structure, city-level revenue, average fare, and time-based revenue mix.
3. `Operations`
   Focuses on active drivers, rider counts, cancellation and no-show rates by city, payment-method mix, and time-of-day trip volume.

This structure separates executive summary, business performance, and operational quality into clearly readable layers without overstating differences that the data does not strongly support.

## 8. Recommendations

1. Use cancellation rate as the lead service-quality KPI and review Boston and Los Angeles most closely.
2. Staff and monitor heavily around `Morning (6-12)` and `Night (0-6)`, the two strongest operating windows.
3. Track Premium fare-tier performance because it contributes the largest share of revenue.
4. Treat city comparisons as monitoring views for exception management, not as evidence of fundamentally different market structures.
5. Preserve the cleaned and Tableau-ready datasets separately so future refreshes remain reproducible and dashboard-safe.

## 9. Final Project Status

The project is complete from a dashboard-development perspective. The remaining work was documentation alignment, which is now covered through:

- a rewritten main `README.md`
- a formal `docs/final_project_documentation.md`
- an updated `docs/data_dictionary.md`
- a refreshed `data_cleaning_report.md`
- a synchronized `tableau/tableau_dashboard_guide.md`
- and this final written report

# Uber Ride-Hailing Operations and Revenue Analysis

This project analyzes Uber trip activity across six U.S. cities to evaluate service reliability, revenue distribution, rider behavior, and operational patterns. The final deliverable is a Tableau Public dashboard portfolio backed by a cleaned trip-level dataset, exploratory analysis, statistical validation, and synchronized project documentation.

## Live Project Links

- Kaggle Dataset: [Uber Trips Dataset - Kaggle](https://www.kaggle.com/datasets/rohiteng/uber-trips-dataset?select=uber_trips_dataset_50k.csv)
- Tableau Public Dashboard: [Uber Analysis Dashboard - Overview](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview)

## Project Snapshot

| Item | Value |
|---|---|
| Raw source rows | 50,000 |
| Cleaned rows | 49,997 |
| Raw columns | 14 |
| Cleaned columns | 23 |
| Tableau-ready columns | 17 |
| Coverage | 2023-01-01 00:00:00 to 2023-02-04 17:19:00 |
| Unique pickup dates | 35 |
| Cities | 6 |
| Unique drivers | 8,963 |
| Unique riders | 38,351 |
| Dataset authenticity | Synthetic sample trip data, not verified real Uber operational trip records |
| Known limitation | GPS coordinates are synthetic and are not used for mapping |

## Dashboard Deliverables

| Asset | Role in the project | Live or local reference |
|---|---|---|
| Tableau Public dashboard | Final interactive business-intelligence deliverable | [Open dashboard](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview) |
| Tableau workbook | Source workbook used to publish the final dashboard | [tableau/workbook/Uber Trips Analysis.twbx](./tableau/workbook/Uber%20Trips%20Analysis.twbx) |
| Dashboard screenshots | Archived dashboard pages for documentation and portfolio use | [tableau/screenshots/](./tableau/screenshots/) |
| Dashboard links reference | Consolidated dashboard URLs and asset notes | [tableau/dashboard_links.md](./tableau/dashboard_links.md) |

## Validated KPI Baseline

The cleaned dataset in `data/processed/uber_cleaned_dataset.csv` is the master business dataset for the project.

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

## Business Insights

### Service Reliability

- Completed trips account for 85.08% of all rides, showing strong overall service completion.
- Cancellations at 9.97% are roughly double the no-show rate of 4.95%, making cancellation the primary operational exception to monitor.
- Boston has the highest cancellation rate at 10.33%, while San Francisco has the lowest at 9.65%.
- Los Angeles has the highest no-show rate at 5.24%, while Boston has the lowest at 4.72%.

### Revenue and City Performance

- Boston generates the highest city revenue at $135,704.41, followed closely by San Francisco at $134,611.24.
- Los Angeles has the lowest city revenue at $131,156.08, but the spread across all six cities remains narrow.
- Seattle records the highest average fare at $16.06, while Los Angeles has the lowest at $15.77.
- Revenue per active driver is tightly clustered, ranging from $23.79 in Los Angeles to $24.88 in Boston.

### Demand and Rider Behaviour

- `Night (0-6)` has the highest trip volume at 12,600 trips, with `Morning (6-12)` close behind at 12,598 trips.
- `Morning (6-12)` produces the highest revenue at $202,099.41, followed by `Night (0-6)` at $200,670.16.
- Weekdays contribute $576,090.41 in revenue versus $222,709.86 on weekends, reflecting the dataset's 72% weekday mix.
- Payment methods are highly balanced: UPI, Card, Wallet, and Cash each contribute close to one quarter of total trip volume.

### Pricing and Statistical Context

- Premium fare-tier trips contribute the largest revenue share at $383,376.89, well above Standard at $258,378.27 and Budget at $157,045.11.
- Fare has a strong positive correlation of 0.871 with both trip distance and trip duration, confirming that pricing largely scales with trip effort.
- Weekday versus weekend fare differences are not statistically meaningful in practice (`p = 0.1366`, `Cohen's d = 0.0148`).
- Fare differences across cities are statistically detectable because the sample is large, but the practical effect is trivial (`eta squared = 0.000284`).
- The association between city and trip status is negligible (`Cramer's V = 0.0083`), so the dashboard is best used for monitoring rather than strong causal claims.

## Dashboard Storyline

The Tableau Public dashboard is organized into three pages:

1. `Overview` for trip volume, total revenue, completion rate, average fare, trip-status mix, daily trend, and city-level trip comparison.
2. `Business Insights` for riders, revenue per driver, city revenue, average fare by city, fare-tier distribution, weekday versus weekend revenue, time-of-day revenue, and fare-tier revenue.
3. `Operations` for active drivers, riders, cancellation rate by city, no-show rate by city, time-of-day trip mix, and payment-method composition.

## Data Foundation

The project uses three closely related datasets:

| File | Purpose |
|---|---|
| [data/raw/uber_raw_dataset.csv](./data/raw/uber_raw_dataset.csv) | Original Kaggle extract |
| [data/processed/uber_cleaned_dataset.csv](./data/processed/uber_cleaned_dataset.csv) | Final cleaned analytical dataset with 23 columns |
| [data/processed/tableau_ready_dataset.csv](./data/processed/tableau_ready_dataset.csv) | Lean 17-column export used in Tableau Public |

## Dataset Authenticity Note

This project treats the source as a synthetic sample ride-hailing dataset rather than verified real Uber trip operations data. The analysis is still useful for dashboard design, KPI structuring, workflow demonstration, and business storytelling, but the findings should be interpreted as portfolio analysis on sample data rather than as conclusions about real Uber operations.

The cleaned dataset preserves the original 14 source columns and adds 9 engineered analysis fields:

- `trip_duration_mins`
- `pickup_date`
- `pickup_hour`
- `pickup_day`
- `pickup_month`
- `pickup_week`
- `time_of_day`
- `fare_per_km`
- `is_weekend`

The Tableau-ready export then adds two business-facing fields during final load preparation:

- `day_type`
- `fare_tier`

## Workflow Summary

1. Raw trip data was collected from Kaggle and stored in `data/raw/`.
2. Python and Pandas were used to validate data quality, standardize text fields, convert datetime columns, remove invalid ghost trips, and engineer analytical features.
3. Jupyter notebooks were used for exploratory analysis, statistical testing, and KPI validation.
4. A final Tableau-ready export was created with only the 17 fields required for dashboard filters, KPIs, and visuals.
5. Tableau Public was used to publish the final three-page dashboard story.

## Repository Structure

```text
Uber_Analysis/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── reports/
├── scripts/
├── tableau/
│   ├── screenshots/
│   └── workbook/
├── data_cleaning_report.md
├── requirements.txt
└── README.md
```

## Recommended Review Order

1. Read this `README.md` for the project summary, KPI baseline, and live dashboard links.
2. Review [docs/final_project_documentation.md](./docs/final_project_documentation.md) for the formal project narrative.
3. Open [reports/project_report.md](./reports/project_report.md) for the polished written report.
4. Explore the Tableau Public dashboard and compare it with the archived screenshots in `tableau/screenshots/`.
5. Use [docs/data_dictionary.md](./docs/data_dictionary.md) and [data_cleaning_report.md](./data_cleaning_report.md) for dataset and transformation details.

## Tools and Technologies

| Tool | Role |
|---|---|
| Python | Data cleaning, validation, and export logic |
| Pandas and NumPy | Data transformation and metric preparation |
| SciPy | Statistical testing |
| Jupyter Notebook | EDA, validation, and workflow documentation |
| Tableau Public | Final interactive dashboard delivery |
| CSV | Raw, cleaned, and Tableau-ready dataset storage |

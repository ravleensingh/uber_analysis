# Uber Data Visualization and Analysis

**Sector:** Transportation / Ride-Hailing  
**Dataset:** Uber Trips (50,000 raw records, January 2023)  
**Tech Stack:** Python, Pandas, NumPy, SciPy, Statsmodels, Matplotlib, Seaborn, Tableau Public  

---

## Business Problem

Ride-hailing platforms generate large volumes of transactional data that, when analysed properly, can reveal actionable patterns in demand, pricing, and service reliability. This project analyses 50,000 Uber trip records across six US cities to answer:

> **What operational patterns in Uber trip data can inform better demand management, pricing strategy, and service reliability decisions?**

**Decision supported:** City-level operational managers can use the insights and dashboard to allocate driver supply, adjust pricing models, and reduce cancellation rates.

---

## Dataset

| Attribute | Details |
|---|---|
| Source | [Kaggle (raw transactional trip records)](https://www.kaggle.com/datasets/rohiteng/uber-trips-dataset?select=uber_trips_dataset_50k.csv) |
| Raw file | `data/raw/uber_trips_dataset_50k.csv` |
| Row count | 50,000 (raw) / 49,997 (cleaned) |
| Column count | 14 (raw) / 23 (cleaned) / 31 (Tableau-ready) |
| Time period | January 2023 (full month) |
| Cities | San Francisco, New York, Chicago, Boston, Seattle, Los Angeles |
| Format | CSV |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Notebook |
|---|---|---|
| Completion Rate | Percentage of trips successfully completed | `03_eda.ipynb` |
| Cancellation Rate | Percentage of trips cancelled by driver or rider | `03_eda.ipynb` |
| No-Show Rate | Percentage of trips where rider did not appear | `03_eda.ipynb` |
| Average Fare per Trip | Mean fare amount across all completed trips | `03_eda.ipynb` |
| Average Trip Duration | Mean trip length in minutes | `03_eda.ipynb` |
| Fare per Kilometre | Fare amount divided by distance -- pricing efficiency | `03_eda.ipynb`, `04_statistical_analysis.ipynb` |
| Peak Hour Volume | Hour of day with the highest trip count | `03_eda.ipynb` |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| Dashboard URL | See [`tableau/dashboard_links.md`](tableau/dashboard_links.md) |
| Executive View | City-level KPI summary -- completion rate, average fare, trip volume |
| Operational View | Drill-down by hour, day, payment method, and trip status |
| Main Filters | City, trip status, payment method, time of day, weekend/weekday |

Screenshots stored in [`tableau/screenshots/`](tableau/screenshots/).

---

## Key Insights

Based on the completed Exploratory Data Analysis and Statistical Analysis:

1. **Service Reliability:** Completed trips dominate the dataset, but a significant volume of cancellations and no-shows presents a critical area for improving service reliability.
2. **Balanced Demand:** Trip volume is distributed evenly across all six cities (San Francisco, New York, Chicago, Boston, Seattle, Los Angeles), indicating a well-balanced operational footprint.
3. **Payment Preferences:** Payment methods (Cash, Card, UPI, Wallet) are split nearly equally, showing diverse user preference and no single dominant payment channel.
4. **Pricing Consistency:** Fare amounts and trip distances have a strong positive correlation, confirming that the distance-driven pricing model functions consistently across regions.
5. **Weekend Surges:** Fares on weekends are statistically significantly higher than on weekdays, demonstrating successful peak/surge pricing implementation.
6. **Commute Dynamics:** Trip duration differs significantly between morning and evening, suggesting heavier traffic patterns during the evening commute.
7. **Localized Efficiency:** Pricing efficiency (Fare per Kilometre) varies significantly by city, suggesting localized pricing dynamics or differing operational costs.
8. **Revenue Concentration:** A Pareto analysis confirms that certain top-performing cities generate a disproportionate amount of revenue, highlighting key areas for operational focus.

---

## Recommendations

Based on the key insights derived from the dataset analysis:

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Significant cancellation rates limit completion volume | Implement targeted cancellation disincentives and optimize routing during peak times | Reduce cancellation rates, directly increasing completed trips and overall revenue |
| 2 | Weekend fares are significantly higher and more lucrative | Proactively optimize driver supply allocation ahead of anticipated weekend surges | Ensure adequate driver supply to capture high-value weekend demand without causing excessive wait times |
| 3 | Pricing efficiency (Fare per KM) varies significantly by city | Conduct localized pricing reviews to standardize margins and ensure regional competitiveness | Improve pricing efficiency and margin consistency across the entire city network |

---

## Repository Structure

```text
Uber_Analysis/
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- data_cleaning_report.md
|
|-- data/
|   |-- raw/
|   |   `-- uber_trips_dataset_50k.csv
|   `-- processed/
|       |-- uber_trips_cleaned.csv
|       `-- uber_trips_tableau_ready.csv
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   |-- __init__.py
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
`-- docs/
    `-- data_dictionary.md
```

---

## Analytical Pipeline

| Step | Phase | Description |
|---|---|---|
| 1 | Extract | Raw dataset loaded and assessed in `01_extraction.ipynb` |
| 2 | Clean | Full cleaning pipeline in `02_cleaning.ipynb` and `scripts/etl_pipeline.py` |
| 3 | Analyse | EDA in `03_eda.ipynb`, statistical analysis in `04_statistical_analysis.ipynb` |
| 4 | Prepare | Tableau-ready export in `05_final_load_prep.ipynb` |
| 5 | Visualise | Dashboard built and published on Tableau Public |
| 6 | Recommend | Business recommendations derived from analysis |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python + Jupyter | ETL, cleaning, analysis, KPI computation |
| Pandas, NumPy | Data manipulation and feature engineering |
| Matplotlib, Seaborn | Exploratory visualizations |
| SciPy, Statsmodels | Hypothesis testing and statistical analysis |
| Tableau Public | Interactive dashboard and storytelling |
| GitHub | Version control and portfolio hosting |

---

## How to Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Run notebooks in order from `01` to `05`.

To run the ETL pipeline from the command line:

```bash
python scripts/etl_pipeline.py \
    --input data/raw/uber_trips_dataset_50k.csv \
    --output data/processed/uber_trips_cleaned.csv
```
# uber_analysis

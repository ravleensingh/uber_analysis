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
| Source | Kaggle (raw transactional trip records) |
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

To be completed after EDA and statistical analysis notebooks are executed.

1. --
2. --
3. --
4. --
5. --
6. --
7. --
8. --

---

## Recommendations

To be completed after analysis.

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | -- | -- | -- |
| 2 | -- | -- | -- |
| 3 | -- | -- | -- |

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

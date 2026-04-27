"""Uber Trips ETL Pipeline.

This script performs the complete Extract-Transform-Load pipeline for the
Uber trips dataset. It loads the raw CSV, applies all cleaning and
transformation steps, engineers derived features, validates the output,
and exports the processed dataset.

Usage:
    python scripts/etl_pipeline.py \
        --input data/raw/uber_trips_dataset_50k.csv \
        --output data/processed/uber_trips_cleaned.csv

Project: Uber Data Visualization and Analysis
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Step 1: Load
# ---------------------------------------------------------------------------

def load_raw_data(input_path: Path) -> pd.DataFrame:
    """Load the raw CSV dataset from the specified path.

    Parameters
    ----------
    input_path : Path
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded dataframe with no modifications.

    Raises
    ------
    FileNotFoundError
        If the input path does not exist.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {input_path}")

    df = pd.read_csv(input_path)
    print(f"[LOAD] Loaded {len(df):,} rows and {df.shape[1]} columns from {input_path.name}")
    return df


# ---------------------------------------------------------------------------
# Step 2: Fix Data Types
# ---------------------------------------------------------------------------

def fix_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Convert columns to appropriate data types.

    Conversions applied:
        - pickup_time, drop_time -> datetime64
        - city, status, payment_method -> category

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with raw string types.

    Returns
    -------
    pd.DataFrame
        Dataframe with corrected types.
    """
    result = df.copy()

    result["pickup_time"] = pd.to_datetime(result["pickup_time"]).dt.round("s")
    result["drop_time"] = pd.to_datetime(result["drop_time"]).dt.round("s")

    for col in ["city", "status", "payment_method"]:
        result[col] = result[col].astype("category")

    print("[DTYPE] Converted datetime and category columns.")
    return result


# ---------------------------------------------------------------------------
# Step 3: Standardize Text
# ---------------------------------------------------------------------------

def standardize_text(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace and apply title case to categorical text columns.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with category columns.

    Returns
    -------
    pd.DataFrame
        Dataframe with standardized text values.
    """
    result = df.copy()
    text_cols = ["city", "status", "payment_method"]

    for col in text_cols:
        result[col] = result[col].str.strip().str.title().astype("category")

    print("[TEXT] Standardized text columns: stripped whitespace, applied title case.")
    return result


# ---------------------------------------------------------------------------
# Step 4: Engineer Features
# ---------------------------------------------------------------------------

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived columns for analysis and dashboarding.

    Derived columns added:
        - trip_duration_mins  : drop_time minus pickup_time in minutes
        - pickup_date         : date portion of pickup_time
        - pickup_hour         : hour (0-23) of pickup_time
        - pickup_day          : day-of-week name (e.g. Monday)
        - pickup_month        : month name (e.g. January)
        - pickup_week         : ISO week number
        - time_of_day         : bucketed segment (Night, Morning, etc.)
        - fare_per_km         : fare_amount / distance_km
        - is_weekend          : True for Saturday and Sunday

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataframe with corrected types.

    Returns
    -------
    pd.DataFrame
        Dataframe with additional derived columns.
    """
    result = df.copy()

    # Trip duration
    result["trip_duration_mins"] = (
        (result["drop_time"] - result["pickup_time"]).dt.total_seconds() / 60
    ).round(2)

    # Date and time components
    result["pickup_date"] = result["pickup_time"].dt.date
    result["pickup_hour"] = result["pickup_time"].dt.hour
    result["pickup_day"] = result["pickup_time"].dt.day_name()
    result["pickup_month"] = result["pickup_time"].dt.month_name()
    result["pickup_week"] = result["pickup_time"].dt.isocalendar().week.astype(int)

    # Time-of-day buckets
    bins = [0, 6, 12, 17, 21, 24]
    labels = [
        "Night (0-6)",
        "Morning (6-12)",
        "Afternoon (12-17)",
        "Evening (17-21)",
        "Night (21-24)",
    ]
    result["time_of_day"] = pd.cut(
        result["pickup_hour"],
        bins=bins,
        labels=labels,
        right=False,
        include_lowest=True,
    ).astype(str)

    # Fare efficiency
    result["fare_per_km"] = np.where(
        result["distance_km"] > 0,
        (result["fare_amount"] / result["distance_km"]).round(4),
        np.nan,
    )

    # Weekend flag
    result["is_weekend"] = result["pickup_time"].dt.dayofweek.isin([5, 6])

    derived = [
        "trip_duration_mins", "pickup_date", "pickup_hour", "pickup_day",
        "pickup_month", "pickup_week", "time_of_day", "fare_per_km", "is_weekend",
    ]
    print(f"[FEATURE] Added {len(derived)} derived columns.")
    return result


# ---------------------------------------------------------------------------
# Step 5: Remove Anomalies
# ---------------------------------------------------------------------------

def remove_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """Remove records with zero distance AND zero duration.

    These are ghost trips -- records created by system errors or failed app
    handshakes. A real trip cannot have both zero distance and zero duration.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with trip_duration_mins already computed.

    Returns
    -------
    pd.DataFrame
        Dataframe with anomalous records removed.
    """
    mask_zero = (df["distance_km"] == 0) & (df["trip_duration_mins"] == 0)
    anomaly_count = mask_zero.sum()

    result = df[~mask_zero].reset_index(drop=True)

    print(f"[ANOMALY] Removed {anomaly_count} ghost trip(s) (zero distance + zero duration).")
    return result


# ---------------------------------------------------------------------------
# Step 6: Validate
# ---------------------------------------------------------------------------

def validate(df: pd.DataFrame) -> None:
    """Run final validation checks and print a summary report.

    Parameters
    ----------
    df : pd.DataFrame
        The fully processed dataframe.

    Raises
    ------
    ValueError
        If any critical validation check fails.
    """
    checks = {
        "Null values remaining": df.isnull().sum().sum(),
        "Duplicate rows": df.duplicated().sum(),
        "Negative fare amounts": (df["fare_amount"] < 0).sum(),
        "Negative distances": (df["distance_km"] < 0).sum(),
        "Negative durations": (df["trip_duration_mins"] < 0).sum(),
        "Drop time before pickup": (df["drop_time"] < df["pickup_time"]).sum(),
    }

    print("\n" + "=" * 60)
    print("  VALIDATION REPORT")
    print("=" * 60)
    all_pass = True
    for check_name, count in checks.items():
        status = "PASS" if count == 0 else f"FAIL ({count})"
        if count > 0:
            all_pass = False
        print(f"  {check_name:<35s} : {status}")
    print("=" * 60)

    if not all_pass:
        failures = {k: v for k, v in checks.items() if v > 0}
        raise ValueError(f"Validation failed on: {list(failures.keys())}")

    print("  All checks passed.\n")


# ---------------------------------------------------------------------------
# Full Pipeline
# ---------------------------------------------------------------------------

def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Execute the full cleaning pipeline from raw CSV to processed dataframe.

    Pipeline order:
        1. Load raw data
        2. Fix data types
        3. Standardize text values
        4. Engineer derived features
        5. Remove anomalous records
        6. Validate final output

    Parameters
    ----------
    input_path : Path
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Fully cleaned and feature-engineered dataframe.
    """
    df = load_raw_data(input_path)
    df = fix_dtypes(df)
    df = standardize_text(df)
    df = engineer_features(df)
    df = remove_anomalies(df)
    validate(df)
    return df


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the processed dataframe to CSV.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataframe to save.
    output_path : Path
        Destination file path.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[SAVE] Exported {len(df):,} rows and {df.shape[1]} columns to {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run the Uber Trips ETL pipeline.",
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw CSV file (e.g., data/raw/uber_trips_dataset_50k.csv).",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path for the cleaned CSV (e.g., data/processed/uber_trips_cleaned.csv).",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for the ETL pipeline."""
    args = parse_args()
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)

    print("\n" + "=" * 60)
    print("  PIPELINE COMPLETE")
    print("=" * 60)
    print(f"  Rows    : {len(cleaned_df):,}")
    print(f"  Columns : {cleaned_df.shape[1]}")
    print(f"  Output  : {args.output}")
    print("=" * 60)


if __name__ == "__main__":
    main()

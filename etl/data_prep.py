import os
from pathlib import Path
import pandas as pd
import numpy as np

# ------------------------
# Paths
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "dataset.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed.csv"

# ------------------------
# Functions
# ------------------------
def load_data(nrows=None):
    """Load raw CSV dataset."""
    try:
        print(f"📂 Loading data from {RAW_DATA_PATH}")
        df = pd.read_csv(RAW_DATA_PATH, nrows=nrows)
        print(f"✅ Loaded shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return None


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop NA, reset index."""
    try:
        print("🧹 Cleaning data ...")
        df = df.dropna().reset_index(drop=True)
        print(f"✅ Cleaned shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Failed to clean data: {e}")
        return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Example feature engineering."""
    try:
        print("⚙️ Feature engineering ...")
        # Example: create a dummy feature if numeric cols exist
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            df["feature_sum"] = df[numeric_cols].sum(axis=1)
        print(f"✅ Features engineered. Columns now: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"❌ Feature engineering failed: {e}")
        return df


def save_processed(df: pd.DataFrame):
    """Save processed data."""
    try:
        df.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"📦 Processed data saved to {PROCESSED_DATA_PATH}")
    except Exception as e:
        print(f"❌ Failed to save processed data: {e}")


def run_etl(nrows=None):
    """ETL pipeline runner."""
    df = load_data(nrows=nrows)
    if df is None:
        return
    df = clean_data(df)
    df = feature_engineering(df)
    save_processed(df)


if __name__ == "__main__":
    run_etl()

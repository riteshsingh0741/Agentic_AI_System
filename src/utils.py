import pandas as pd
import os

def ensure_data_dir():
    """Ensure data and reports folders exist."""
    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

def read_csv(file_path: str):
    """Read CSV and return list of (id, story)."""
    df = pd.read_csv(file_path)
    if "id" not in df.columns or "story" not in df.columns:
        raise ValueError("CSV must contain 'id' and 'story' columns.")
    return list(zip(df["id"], df["story"]))

def save_csv(ids, stories, file_path: str):
    """Save refined stories with their IDs."""
    pd.DataFrame({"id": ids, "story": stories}).to_csv(file_path, index=False)

import pandas as pd
from pathlib import Path

RAW_DIR = Path("../data/raw")
PROCESSED_DIR = Path("../data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILE = RAW_DIR / "sample_csv.csv"

def process_csv():
    df = pd.read_csv(CSV_FILE)

    df.columns = df.columns.str.lower().str.strip()
    df = df.drop_duplicates()

    output_path = PROCESSED_DIR / "sample_data_cleaned.csv"
    df.to_csv(output_path, index=False)

    print(f"Processed CSV file saved -> {output_path}.")

if __name__ == "__main__":
    process_csv()


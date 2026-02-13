import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import confidential as con

# ---------------- CONFIG ----------------
DB_USER = con.DB_USER
DB_PASSWORD = con.DB_PASSWORD
DB_HOST = con.DB_HOST
DB_PORT = con.DB_PORT
DB_NAME = con.DB_NAME
TABLE_NAME = con.TABLE_NAME
temp_path = con.temp_path
# CSV_FILE = Path("single_row.csv")
def create_csv(recent_temp):
    path = temp_path
    with open(path, 'w') as file:
        file.write(recent_temp)
        # print(recent_temp, 'is written')
    return path

def convert_types(df):
    df = df.copy()

    # floats
    float_cols = [
        "latitude", "longitude", "generationtime_ms",
        "elevation", "temperature", "windspeed"
    ]
    for col in float_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # integers
    int_cols = [
        "utc_offset_seconds", "interval",
        "winddirection", "weathercode"
    ]
    for col in int_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # booleans (0/1 or true/false)
    df["is_day"] = (
        df["is_day"]
        .map({"1": True, "0": False, 1: True, 0: False, True: True, False: False})
        .astype("boolean")
    )

    # datetime
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # strings
    string_cols = ["timezone", "timezone_abbreviation"]
    for col in string_cols:
        df[col] = df[col].astype("string").str.strip()

    return df


# ---------------- LOAD SINGLE RECORD ----------------
def load_single_record(CSV_FILE):
    # Read CSV (header = column names)

    df = pd.read_csv(CSV_FILE)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    # safety check to check csv is full or empty
    if df.empty:
        raise ValueError("CSV file contains no data")
    # Create DB engine
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print("\nEngine Created..\n")
    # Scema change
    df = convert_types(df)
    # Insert data
    value = df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",
        index=False
    )
    # print(value) tmeporary for debugging
    print(f"{len(df)} row(s) inserted into {TABLE_NAME}")

def main(recent_temp):
    csv = create_csv(recent_temp[0:-1])
    load_single_record(csv)
    return True
# ---------------- MAIN ----------------
if __name__ == "__main__":
    main()

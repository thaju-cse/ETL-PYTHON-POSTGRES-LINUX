import requests
import json
from datetime import datetime
from pathlib import Path
import confidential as con

RAW_DIR = con.RAW_DIR
PROCESSED_DIR = con.PROCESSED_DIR
API_URL = con.API_URL
PARAMS = con.PARAMS

def fetch_weather():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    return response.json()

def save_raw_json(data):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    # timestamp = datetime.datetime.now(datetime.UTC)
    file_path = RAW_DIR / f"weather_{timestamp}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved raw API data -> {file_path}.\n")
    return file_path


def main():
    weather_data = fetch_weather()
    file_path = save_raw_json(weather_data)
    return file_path

if __name__ == "__main__":
    main()

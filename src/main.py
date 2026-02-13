import weather_api
import json_to_csv
import csv_to_postgres
from pathlib import Path

def main():
    RAW_DIR = Path("../data/raw")
    PROCESSED_DIR = Path("../data/processed")
    # RAW_DIR.mkdir(parents=True, exist_ok=True)
    API_URL = "https://api.open-meteo.com/v1/forecast"
    PARAMS = {
        "latitude": 12.8934,
        "longitude": 77.6258,
        "current_weather": True
        }
    # Calling Weather data extracting function
    json_file_path = weather_api.main(RAW_DIR, API_URL, PARAMS)
    # Weather_api returns json file file which is further used to transform into a csv file
    csv_file_path = PROCESSED_DIR / f"weather_{PARAMS['latitude']}_{PARAMS['longitude']}.csv"
    # custom made csv file path with latitude and longitude in the file name
    recent_temp = json_to_csv.main(json_file_path, csv_file_path)
    status = csv_to_postgres.main(recent_temp)
    print("\n*** Completed ***.")

if __name__=="__main__":
    main()

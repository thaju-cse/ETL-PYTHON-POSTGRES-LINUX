import requests
import json
from datetime import datetime
from pathlib import Path

RAW_DIR = Path("../data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
	"latitude": 12.8934,
	"longitude": 77.6258,
	"current_weather": True
}


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
    print(f"Saved raw API data -> {file_path}.")

if __name__ == "__main__":
    weather_data = fetch_weather()
    save_raw_json(weather_data)

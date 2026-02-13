import weather_api
import json_to_csv
import csv_to_postgres
import staging_postgres
from pathlib import Path

def main():

    # Calling Weather data extracting function
    json_file_path = weather_api.main()
    print("\nJson file extracted successfully.\n")

    # Load raw json file into the database of the postgres warehouse
    status = staging_postgres.main(json_file_path)
    print(f"\nData inserted into staging table status: {status}\n")

    # custom made csv file path with latitude and longitude in the file name
    recent_temp = json_to_csv.main(json_file_path)
    print("\nCSV file created with latest data.\n")

    # Loading data into the postgres database
    status = csv_to_postgres.main(recent_temp)
    print(f"\nLoading process status: {status}\n")

    print("\n*** Completed ***.\n")

if __name__=="__main__":
    main()

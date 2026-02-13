import confidential as con
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

DB_USER = con.DB_USER
DB_PASSWORD = con.DB_PASSWORD
DB_HOST = con.DB_HOST
DB_PORT = con.DB_PORT
DB_NAME = con.DB_NAME
TABLE_NAME = con.STAGING_TABLE_NAME


def stage(json_file_path):
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    df = pd.read_json(json_file_path)
    time_stamp = pd.to_datetime(df.current_weather['time'], errors = 'coerce')
    # print(time_stamp)
    data = ''
    with open(json_file_path, 'r') as json:
        # data = ''
        for i in json:
            data = data + i
        # print(data)

    DATA = [[time_stamp, data]]

    df = pd.DataFrame(DATA, columns = ['timestamp', 'data'])
    status = df.to_sql(
		TABLE_NAME, 
		engine,
		if_exists = 'append', 
		index = False
		)

    return status

def main(json_file_path):
    # def main():
    # json_file_path = Path('../data/raw/weather_20260212_064414.json')
    status = stage(json_file_path)
    return status

if __name__ == "__main__":
    main()

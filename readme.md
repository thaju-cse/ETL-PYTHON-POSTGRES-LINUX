# Incremental-ETL-with-Data-Quality-Partitioning

This is a project where we will get a current weather JSON file from open weather api,
then stored in database which acts as a data warehouse for this project after that 
performed simple transformations, store in a csv file then finally uploading every new 
entry into a table located in postgresql database.

---

## Overview
This project demonstrates API based data extracting in JSON file format, basic transformations 
like removing white spaces, upper case to lower case then stored in a csv file finally stored 
in a database and everuthing done by using python.

---

## Features
- Real-time weather data fetching using APIs.
- Basic transformations of CSV files.
- Incremental loading into postgresql database

---

## Tech Stack
```
|---------------------------------------------------------|
|Category       |Tools                                    |
|_______________|_________________________________________|
|Language       |Python                                   |
|Libraries      |requests, pandas, datetime, json, pathlib|
|               |sqlalchemy, sys                          |
|OS             |Ubuntu(WSL)                              |
|DBMS           |Postgres                                 |
|Files          |CSV, JSON                                |
|---------------------------------------------------------|
```
---

## Project Architecture
1. Fetch weather data from API
2. Store raw data into a JSON file
3. Transform into a csv file
4. Incremetal loading into postgres for every new entry

---

## Installation
```bash
git clone https://github.com/thaju-cse/Incremental-ETL-with-Data-Quality-Partitioning
cd Incremental-ETL-with-Data-Quality-Partitioning
pip install -r requirements.txt
cd src
python3 main.py
```
---

## Folder Structure
```
Incremental-ETL-with-Data-Quality-Partitioning
.
├── data
│   ├── processed
│   │   ├── recent.csv
│   │   └── weather_14.5119_79.4112.csv
│   └── raw
│       └── weather_20260212_091256.json
├── images
│   ├── Staging.png
│   └── Weather.png
├── readme.md
├── requirements.txt
└── src
    ├── __pycache__
    │   ├── confidential.cpython-312.pyc
    │   ├── csv_to_postgres.cpython-312.pyc
    │   ├── json_to_csv.cpython-312.pyc
    │   ├── staging_postgres.cpython-312.pyc
    │   └── weather_api.cpython-312.pyc
    ├── confidential.py
    ├── csv_to_postgres.py
    ├── json_to_csv.py
    ├── main.py
    ├── staging_postgres.py
    └── weather_api.py
7 directories, 16 files

```
---

## Learning Outcomes
- Hands on experience in requests,sqlalchemy and pandas modules
- Hands on experience in databases of postgres
- Hands on experience in file handling (csv,json)

---

## Future Enhancements
- Implementation of structured approach to complete the pipeline
- Making data more reliable by doing advanced transformations
- Visualizing the work i had done using tools

---

## Challenges
- Finding the actual problem in the pripeline
- Tightly coupling the functions
- Connection error with the database
- Incremental loading and maintaining the time stamps

---

## Author
**Shaik Thajuddhin**
---
**Aspiring Data Engineer**

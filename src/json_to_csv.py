import pandas as pd
import json
import sys

def json_to_csv_pandas(json_file_path, csv_file_path):
    # Open the JSON file and load its data
    temp = ""
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        '''columns = latitude,longitude,generationtime_ms,utc_offset_seconds,timezone,timezone_abbreviation,elevation,time,interval,temperature,windspeed,winddirection,is_day,weathercode,'''
        
        with open(csv_file_path,'a') as csv:
            # c.write(str(data['latitude']))
            keys = data.keys()
            c = 0
            temp = "latitude,longitude,generationtime_ms,utc_offset_seconds,timezone,timezone_abbreviation,elevation,time,interval,temperature,windspeed,winddirection,is_day,weathercode,\n"
            # Need to add a temp csv file to add into a database while uploading into csv file
            for i in keys:
                
                if i == 'current_weather_units':
                    continue
                elif i == 'current_weather':
                    weather = data['current_weather']
                    weather_keys = weather.keys()
                    for j in  weather_keys:
                        c += 1
                        csv.write(str(weather[j])+',')
                        temp = temp+str(weather[j])+','
                    csv.write('\n')
                    continue
                else:
                    csv.write(str(data[i])+',')
                    temp = temp+str(data[i])+','
                c += 1
            print(f"Found {c} columns values to insert into csv,\n")
        # print(data.keys())
        # print(data.values())
        # print("\n", data["current_weather_units"], "\n\n", data['current_weather'])

        # print(type(data["current_weather_units"]), type(data['current_weather']))
        '''print(data)
        print(type(data))
        print(str(data))
        for i in data:
            print(i)
            print(type(i))'''
    # Use json_normalize to flatten the data into a DataFrame
    # For simple, non-nested JSON, pd.read_json might be sufficient
    # We use json_normalize for better handling of potential nesting
    # df = pd.json_normalize(data)
    
    # Write the DataFrame to a CSV file
    # df.to_csv(csv_file_path, encoding='utf-8', index=False)
    print(f"Successfully inserted data of {json_file_path} into {csv_file_path}\n")
    return temp
def main(json_file_path, csv_file_path ):

    json_file = json_file_path
    csv_file = csv_file_path
    temp = json_to_csv_pandas(json_file, csv_file)
    return temp
if __name__=="__main__":
    main()

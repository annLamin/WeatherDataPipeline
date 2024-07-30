import requests
import pandas as pd
from datetime import datetime, timedelta

def run_openweather_etl():
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    lat = 42.35
    lon = 13.39
    start_date = datetime(2022, 7, 1)
    end_date = datetime(2024, 7, 27)

    # Generate timestamps for each day in the range
    timestamps = []
    current_date = start_date
    while current_date <= end_date:
        timestamp = int(current_date.timestamp())
        timestamps.append(timestamp)
        current_date += timedelta(days=1)

    # List to accumulate weather data
    weather_data = []

    for timestamp in timestamps:
        # Construct the URL with the correct spelling of 'exclude'
        url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&exclude=minutely,hourly&appid={api_key}&units=imperial"

        response = requests.get(url)
        data = response.json()
        print(data)
        # Extract relevant data
        timezone = data.get('timezone', 'N/A')
        current = data.get('current', {})
        # print(current.temp)
        data_list = data.get('data', [])

        for entry in data_list:
            timestamp = entry.get('dt', 'N/A')
            temp = entry.get('temp', 'N/A')
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d') if timestamp != 'N/A' else 'N/A'
            
            weather_data.append({
                "timezone": timezone,
                "date": date,
                "temperature": temp
            })

    # Convert to DataFrame
    df = pd.DataFrame(weather_data)

    # Export the DataFrame to a CSV file
    
    csv_file = 'weather_data.csv'
    df.to_csv(f'data saved in {csv_file}')
    # for saving in s3
    # df.to_csv('s3://lamin-airflow-bucket/weather_data.csv')

    print(f"Data saved to {csv_file}")

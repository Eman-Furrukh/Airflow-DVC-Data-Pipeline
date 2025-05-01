import requests
import pandas as pd
from datetime import datetime

API_KEY = "44abdcb2f9e76a43e7f9c363528ea83c"
CITY = "London"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": CITY,
    "units": "metric",  # Temperature in Celsius
    "cnt": 5,  # Number of days
    "appid": API_KEY,
}

response = requests.get(BASE_URL, params=params)
data = response.json()

# Extract relevant fields and structure the data
weather_data = []
for entry in data['list']:
    weather_data.append({
        "Temperature": entry['main']['temp'],
        "Humidity": entry['main']['humidity'],
        "Wind Speed": entry['wind']['speed'],
        "Weather Condition": entry['weather'][0]['description'],
        "Date and Time": datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'),
    })

# Save the data to a CSV file
df = pd.DataFrame(weather_data)
df.to_csv('raw_data.csv', index=False)


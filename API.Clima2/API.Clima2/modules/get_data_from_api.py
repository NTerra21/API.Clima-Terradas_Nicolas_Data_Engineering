import requests
from io import StringIO
import pandas as pd
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::GetDataModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

class DataRetriever:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cities = ["London", "New York", "Tokyo", "Sydney", "Paris"]
    
    def get_data(self):
        data_list = []
        for city in self.cities:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data_list.append(response.json())
            else:
                logging.error(f"Failed to retrieve data for {city}: {response.status_code}")
        
        data = []
        for entry in data_list:
            city_data = {
                'city': entry['name'],
                'temperature': entry['main']['temp'],
                'humidity': entry['main']['humidity'],
                'pressure': entry['main']['pressure'],
                'weather': entry['weather'][0]['description'],
                'wind_speed': entry['wind']['speed'],
                'timestamp': pd.to_datetime(entry['dt'], unit='s')
            }
            data.append(city_data)
        
        try:
            data = pd.DataFrame(data)
            buffer = StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            logging.info(s)
            logging.info("Data created")
            return data
        
        except Exception as e:
            logging.error(f"Not able to import the data from the api\n{e}")
            raise

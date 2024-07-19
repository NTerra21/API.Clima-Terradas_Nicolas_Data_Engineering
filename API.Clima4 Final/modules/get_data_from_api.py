import requests
import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::GetDataModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

class DataRetriever:
    def __init__(self):
        self.api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        self.cities = ["London", "New York", "Tokyo"]

    def get_data(self):
        data_list = []
        for city in self.cities:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            )
            data = response.json()
            city_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather_description": data["weather"][0]["description"],
                "data_retrieval_time": datetime.utcnow(),
                "data_generation_time": datetime.fromtimestamp(data["dt"]),
            }
            data_list.append(city_data)

        df = pd.DataFrame(data_list)
        logging.info(f"Weather data retrieved: {df}")
        return df
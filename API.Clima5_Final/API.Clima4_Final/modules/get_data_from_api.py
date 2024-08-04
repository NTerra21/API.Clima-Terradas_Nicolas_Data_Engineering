import requests
from io import StringIO
import pandas as pd
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::GetDataModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

class DataRetriever:
    def __init__(self, city: str = "London") -> None:
        self.api_key = os.getenv('YOUR_OPENWEATHERMAP_API_KEY')
        self.endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
    
    def get_data(self):
        response_json = requests.get(self.endpoint).json()
        data_by_list_api = pd.DataFrame([response_json])
        cols = ["id", "name", "main.temp", "main.humidity", "wind.speed", "dt"]
        logging.info(f"{cols} -> to be inserted")
        
        try:
            data = data_by_list_api[cols]
            data = data.fillna(0)
            buffer = StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            logging.info(s)
            logging.info("Data created")
            return data
        
        except Exception as e:
            logging.error(f"Not able to import the data from the api\n{e}")
            raise
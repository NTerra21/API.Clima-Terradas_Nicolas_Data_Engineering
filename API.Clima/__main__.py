import os
import logging
from modules import DataConn , DataRetriever
from dotenv import load_dotenv

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::MainModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

def main():
    config = {
        'REDSHIFT_USERNAME': os.getenv('REDSHIFT_USERNAME'),
        'REDSHIFT_PASSWORD': os.getenv('REDSHIFT_PASSWORD'),
        'REDSHIFT_HOST': os.getenv('REDSHIFT_HOST'),
        'REDSHIFT_PORT': os.getenv('REDSHIFT_PORT'),
        'REDSHIFT_DBNAME': os.getenv('REDSHIFT_DBNAME')
    }
    schema = 'andru_ocatorres_coderhouse'
    
    data_conn = DataConn(config=config, schema=schema)
    data_conn.get_conn()
    
    data_retriever = DataRetriever()
    data = data_retriever.get_data()
    
    table_name = 'weather_data'
    data_conn.upload_data(data, table=table_name)
    
    data_conn.close_conn()

if __name__ == "__main__":
    main()
import os
from subprocess import call
from modules.data_con import DataConn
from modules.get_data_from_api import DataRetriever
from dotenv import load_dotenv

load_dotenv()

def run_sql_script(script_path):
    command = f"psql -h {os.getenv('REDSHIFT_HOST')} -d {os.getenv('REDSHIFT_DBNAME')} -U {os.getenv('REDSHIFT_USERNAME')} -p {os.getenv('REDSHIFT_PORT')} -f {script_path}"
    os.system(command)

def main():
    # Correr los scripts de seguridad
    run_sql_script('sql_scripts/Seguridad_basica_Redshift.sql')
    run_sql_script('sql_scripts/Seguridad_columnas_Redshift.sql')
    
    config = {
        'REDSHIFT_USERNAME': os.getenv('REDSHIFT_USERNAME'),
        'REDSHIFT_PASSWORD': os.getenv('REDSHIFT_PASSWORD'),
        'REDSHIFT_HOST': os.getenv('REDSHIFT_HOST'),
        'REDSHIFT_PORT': os.getenv('REDSHIFT_PORT'),
        'REDSHIFT_DBNAME': os.getenv('REDSHIFT_DBNAME')
    }
    schema = 'nicolas_terradas_coderhouse'
    
    data_conn = DataConn(config=config, schema=schema)
    data_conn.get_conn()
    
    data_retriever = DataRetriever()
    data = data_retriever.get_data()
    
    table_name = 'weather_data'
    data_conn.upload_data(data, table=table_name)
    
    data_conn.close_conn()

if __name__ == "__main__":
    main()

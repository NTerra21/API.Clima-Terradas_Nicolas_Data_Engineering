FROM python:3.8-slim

RUN pip install apache-airflow pandas psycopg2 requests python-dotenv

COPY sql_scripts /sql_scripts
COPY dag /dag
COPY Modules /Modules
COPY .env /
COPY main.py /

ENTRYPOINT ["python", "main.py"]
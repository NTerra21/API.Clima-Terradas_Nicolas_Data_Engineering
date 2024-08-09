FROM apache/airflow:2.9.3
ADD requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install apache-airflow==2.9.3 -r requirements.txt-
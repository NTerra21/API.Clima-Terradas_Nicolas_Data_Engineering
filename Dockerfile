FROM python:3.9-slim

# Install Airflow dependencies
RUN pip install apache-airflow

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /API.CLIMA4_FINAL

# Set the working directory
WORKDIR /API.CLIMA4_FINAL

# Set environment variables
ENV AIRFLOW_HOME=/API.CLIMA4_FINAL/airflow

# Initialize Airflow
RUN airflow db init

# Copy DAGs to the appropriate directory
COPY dag/ /API.CLIMA4_FINAL/airflow/dags/

# Set entrypoint
ENTRYPOINT ["airflow", "scheduler"]
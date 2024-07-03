# Usar una imagen base de Python ligera
FROM python:3.9-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Apache Airflow
RUN pip install apache-airflow

# Comando para iniciar Airflow
CMD ["airflow", "scheduler"]
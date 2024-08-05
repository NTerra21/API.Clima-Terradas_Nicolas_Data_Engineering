# Weather Data ETL Project

## Descripción
Este proyecto extrae datos meteorológicos de la API de OpenWeatherMap, los transforma y los carga en una base de datos Redshift. El objetivo es automatizar este proceso utilizando Apache Airflow y contenedores Docker.




## Instrucciones de Uso

### Configuración del Entorno
1. Clonar el repositorio.
2. Crear un archivo `.env` con las siguientes variables:
    ```
    REDSHIFT_USERNAME=nicolasterradas123_coderhouse
    REDSHIFT_PASSWORD=48a3QLImmc
    REDSHIFT_HOST=data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com
    REDSHIFT_PORT=5439
    REDSHIFT_DBNAME=data-engineer-database
    YOUR_OPENWEATHERMAP_API_KEY=80078194ebdb0d0eb0b5ed04317f344f
    ```

### Construcción y Ejecución del Contenedor Docker
1. Construir la imagen Docker:
    ```sh
    docker-compose build
    ```
2. Iniciar los servicios de Airflow:
    ```sh
    docker-compose up
    ```

### Ejecución del DAG
1. Acceder a la interfaz de Airflow en `http://localhost:8080`.
2. Activar y ejecutar el DAG `weather_data_etl`.

## Detalles Técnicos

### Extracción de Datos
El script `get_data_from_api.py` se encarga de extraer datos de la API de OpenWeatherMap y transformarlos en un DataFrame de Pandas.

### Transformación de Datos
La transformación de datos se realiza mediante Pandas para asegurar la correcta estructuración de la información antes de su carga en Redshift.

### Carga de Datos
El módulo `data_con.py` gestiona la conexión a Redshift y la inserción de los datos en la tabla `weather_data`.

### Seguridad
Se implementan medidas básicas de seguridad para la gestión de usuarios y permisos en Redshift a través de los scripts SQL en la carpeta `sql_scripts`.

### Alertas
El sistema envía alertas por correo electrónico si se detectan valores que sobrepasen ciertos límites configurados en el código.

## Notas Adicionales
- Asegúrate de que todas las dependencias estén actualizadas y sean compatibles.
- Revisa y adapta los scripts SQL según sea necesario para tu entorno específico.

# Esto creará un nuevo usuario con el rol de administrador.
airflow users create --username myuser --password mypassword --firstname John --lastname Doe --email johndoe@miempresa.com --role ADM

# Donde /path/to/user.json es el camino al archivo JSON que contiene la información del usuario.
airflow users create --json /path/to/user.json

--username: El nombre de usuario que deseas crear.
--password: La contraseña que deseas asignar al usuario.
--firstname: El nombre del usuario.
--lastname: El apellido del usuario.
--email: La dirección de correo electrónico del usuario.
--role: El rol que deseas asignar al usuario (por ejemplo, Admin, Operator, Viewer, etc.).

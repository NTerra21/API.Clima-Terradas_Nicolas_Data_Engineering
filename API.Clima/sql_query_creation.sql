DROP TABLE IF EXISTS andru_ocatorres_coderhouse.weather_data;

CREATE TABLE weather_data (
    city VARCHAR(250),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather VARCHAR(250),
    wind_speed FLOAT,
    timestamp TIMESTAMP
);
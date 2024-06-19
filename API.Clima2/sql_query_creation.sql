DROP TABLE IF EXISTS federico_terradas_coderhouse.weather_data;

CREATE TABLE federico_terradas_coderhouse.weather_data (
    city VARCHAR(250),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather VARCHAR(250),
    wind_speed FLOAT,
    timestamp TIMESTAMP
);
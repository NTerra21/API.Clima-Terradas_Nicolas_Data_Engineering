CREATE SCHEMA IF NOT EXISTS nicolas_terradas_coderhouse;

CREATE TABLE IF NOT EXISTS nicolas_terradas_coderhouse.weather_data (
    city VARCHAR(50),
    country VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    weather_description VARCHAR(100),
    data_retrieval_time TIMESTAMP,
    data_generation_time TIMESTAMP,
    PRIMARY KEY (city, data_generation_time)
);

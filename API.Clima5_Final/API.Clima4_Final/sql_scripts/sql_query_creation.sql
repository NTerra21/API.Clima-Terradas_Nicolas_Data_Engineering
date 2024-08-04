DROP TABLE IF EXISTS nicolas_terradas_coderhouse.weather_data;

CREATE TABLE nicolas_terradas_coderhouse.weather_data (
    city VARCHAR(250),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather VARCHAR(250),
    wind_speed FLOAT,
    timestamp TIMESTAMP SORTKEY,
    PRIMARY KEY (city, timestamp)
)
diststyle all;

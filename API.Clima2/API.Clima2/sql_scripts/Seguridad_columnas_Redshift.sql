-- Momento 1: Otorgar acceso al usuario para todas las columnas, excepto las que contengan datos sensibles para el usuario
GRANT ALL ON SCHEMA nicolas_terradas_coderhouse TO data_scientist;
GRANT SELECT(city, temperature, humidity, pressure, weather, wind_speed, timestamp) ON nicolas_terradas_coderhouse.weather_data TO data_scientist;

-- Momento 2: Conectarse al cluster con usuario data_scientist.
-- Ejecute una seleccion en la tabla con y sin las columnas con acceso restringido. Observe la diferencia.
SELECT city, temperature, humidity, pressure, weather, wind_speed, timestamp
FROM nicolas_terradas_coderhouse.weather_data;

SELECT city, temperature, humidity, pressure, weather, wind_speed, timestamp
FROM nicolas_terradas_coderhouse.weather_data;
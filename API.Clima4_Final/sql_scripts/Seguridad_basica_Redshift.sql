-- Momento 1
CREATE SCHEMA nicolas_terradas_coderhouse_secure;

CREATE TABLE nicolas_terradas_coderhouse_secure.my_secure_table (
name VARCHAR(30),
dob TIMESTAMP SORTKEY,
zip INTEGER,
ssn VARCHAR(9)
)
diststyle all;

-- Momento 2
CREATE USER data_scientist PASSWORD 'Test1234';

CREATE GROUP ds_prod WITH USER data_scientist;

-- Momento 3
SELECT * FROM nicolas_terradas_coderhouse_secure.my_secure_table;
-- Run this code segment in the psql shell to set up database.
-- Running this code after the database has been created will clear all data.

DROP DATABASE IF EXISTS smartschedule;
CREATE DATABASE smartschedule;

DROP USER IF EXISTS MAB;
CREATE USER MAB WITH PASSWORD 'mab19';
GRANT ALL PRIVILEGES ON DATABASE smartschedule TO MAB;
ALTER DATABASE smartschedule OWNER TO MAB



	
	


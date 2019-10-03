-- Run this in SQL shell to set up database tables
-- Not that running will clear all tables first.

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS adminfor;
DROP TABLE IF EXISTS worksfor;
DROP TABLE IF EXISTS availability;

CREATE TABLE users(
	email VARCHAR(127) PRIMARY KEY,
	name VARCHAR(127),
	phone VARCHAR(15)
);

CREATE TABLE companies(
	companyid INT PRIMARY KEY,
	name VARCHAR(127),
	location VARCHAR(255)
);

CREATE TABLE adminfor(
	companyid INT,
	email VARCHAR(127)
);

CREATE TABLE worksfor(
	companyid INT,
	email VARCHAR(127),
	role VARCHAR(127),
	startdate VARCHAR(31)
);

CREATE TABLE availability(
	companyid INT,
	email VARCHAR(127),
	role VARCHAR(127),
	day_ DATE,
	starttime TIME,
	endtime TIME
);

-- add test data below




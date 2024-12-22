DROP DATABASE IF EXISTS Binusantara;
CREATE DATABASE Binusantara;
USE Binusantara;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE Customer(
	customerID			CHAR(10)		PRIMARY KEY,
    `customer_fname`	VARCHAR(255)	NOT NULL,
    `customer_lname`	VARCHAR(255)	NOT NULL,
    `customer_email`	VARCHAR(255)	NOT NULL,
	`customer_phoneNo`	VARCHAR(255)	NOT NULL,
    `customer_sex`		CHAR(1)			NOT NULL,
    `customer_DOB`		DATE			NOT NULL,
    `customer_ppNo`		VARCHAR(255)	NOT NULL,
    
    CHECK(`customer_sex` LIKE 'M' OR 'F'),
    CHECK(`customer_email` LIKE '%@%')
);

CREATE TABLE Staff(
	staffID 			CHAR(10) 		PRIMARY KEY,
    `staff_fname` 		VARCHAR(255)	NOT NULL,
    `staff_lname` 		VARCHAR(255)	NOT NULL,
    `staff_email`		VARCHAR(255)	NOT NULL,
    `staff_phoneNo`		VARCHAR(255)	NOT NULL,
    `staff_sex`			CHAR(1)			NOT NULL,
    `staff_salary`		INT				NOT NULL,
    
    CHECK(`staff_sex` LIKE 'M' OR 'F'),
    CHECK(`staff_email` LIKE '%@binusantara.org')
);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
CREATE TABLE Tour(
	tourID				CHAR(10)		PRIMARY KEY,
    `tour_name`			VARCHAR(255)	NOT NULL,
    `start_date`		DATE 			NOT NULL,
    `end_date`			DATE 			NOT NULL,
    `tour_price`		INT				NOT NULL,
    `tour_desc`			VARCHAR(1000)	,
    
    CHECK(`start_date` > SYSDATE() AND `end_date` > SYSDATE())
);

CREATE TABLE Destination(
	destID				CHAR(10)		PRIMARY KEY,
    `dest_name`			VARCHAR(255)	NOT NULL,
    `country`			VARCHAR(255)	NOT NULL,
    `address`			VARCHAR(255)	NOT NULL,
    `dest_desc`			VARCHAR(255)	
);

CREATE TABLE TourDest(
	tourID				CHAR(10)		NOT NULL,
    destID				CHAR(10)		NOT NULL,
    
    PRIMARY KEY (tourID, destID)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE Flight(
	flightID			CHAR(10)		PRIMARY KEY,
    `airline_name`		VARCHAR(255)	NOT NULL,
    `dep_airport`		VARCHAR(255)	NOT NULL,
    `dep_time`			TIME			NOT NULL,
    `arr_airport`		VARCHAR(255)	NOT NULL,
    `arr_time`			TIME			NOT NULL
);

CREATE TABLE Booking(
	bookingID			CHAR(10)		PRIMARY KEY,
    customerID			CHAR(10)		NOT NULL,
    `booking_date`		DATE			NOT NULL,
    `status`			VARCHAR(255)	NOT NULL,
    tourID				CHAR(10)		NOT NULL,
    staffID				CHAR(10)		,
    
    FOREIGN KEY (customerID) 	REFERENCES Customer(customerID),
    FOREIGN KEY (tourID) 		REFERENCES Tour(tourID),
    FOREIGN KEY (staffID)		REFERENCES Staff(staffID),
    
    CHECK(`booking_date` > SYSDATE())
);

CREATE TABLE FlightBooking(
    bookingID			CHAR(10)		NOT NULL,
    flightID			CHAR(10)		,
    `seats`				INT				NOT NULL,
    `class`				VARCHAR(255)	NOT NULL,
     
    PRIMARY KEY (bookingID, flightID),
    CHECK (`seats` BETWEEN 1 AND 20),
    CHECK (`class` LIKE 'Economy' OR 'Business' OR 'First')
);
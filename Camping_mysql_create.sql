CREATE DATABASE Camping;
USE Camping;




CREATE TABLE `Booking` (
    `Id` INT(10) NOT NULL,
    `Customer Id` INT(10) NOT NULL,
    `Position Id` INT(10) NOT NULL,
    `Due date of arrival` DATE NOT NULL,
    `Due date of departure` DATE NOT NULL,
    `Advance` INT(10),
    `Total Cost` INT(10),
    `Condition` VARCHAR(10) ,
	`Booking Date` DATE,
    PRIMARY KEY (`Id`)
);

CREATE TABLE `Customers` (
	`Id` INT(10) NOT NULL,
	`Full name` VARCHAR(100) ,
	`ResId` INT(10),
	`Phone number` VARCHAR(100) ,
	`Birthdate` DATE ,
	`ADT` VARCHAR(15) UNIQUE,
	`Cost per day` FLOAT(10) NOT NULL,
	`Total cost` FLOAT(50),
	PRIMARY KEY (`Id`)
);

CREATE TABLE `Position` (
	`Id` INT(10) NOT NULL,
	`Type` VARCHAR(50) ,
	`Usage Cost` FLOAT(5) ,
	`Electricity` VARCHAR(5) ,
	`Wifi` VARCHAR(5) ,
	`Available for annual book` VARCHAR(3) ,
	`Max number` INT(2) ,
	PRIMARY KEY (`Id`)
);


CREATE TABLE `CheckIn` (
	`Booking Id` INT(10) NOT NULL,
	`Arrival Date` DATE NOT NULL,
	`Due date of departure` DATE NOT NULL
);

ALTER TABLE `Customers` ADD CONSTRAINT `Customers_fk0` FOREIGN KEY (`ResId`) REFERENCES `Customers`(`Id`) ON DELETE CASCADE ;

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk0` FOREIGN KEY (`Customer Id`) REFERENCES `Customers`(`Id`) ON DELETE CASCADE;

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk1` FOREIGN KEY (`Position Id`) REFERENCES `Position`(`Id`) ON DELETE CASCADE;

ALTER TABLE `CheckIn` ADD CONSTRAINT `CheckIn_fk0` FOREIGN KEY (`Booking Id`) REFERENCES `Booking`(`Id`) ON DELETE CASCADE;




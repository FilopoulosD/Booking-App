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
	`Max number` INT(2) ,
	PRIMARY KEY (`Id`)
);

CREATE TABLE `CheckIn` (
	`Position Id`  INT(10),
	`Customers Id` INT(10),
	`Arrival Date` DATE NOT NULL,
	`Due date of departure` DATE NOT NULL,
	PRIMARY KEY (`Position Id`, `Customers Id`,`Arrival Date`)
);


ALTER TABLE `Customers` ADD CONSTRAINT `Customers_fk0` FOREIGN KEY (`ResId`) REFERENCES `Customers`(`Id`);

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk0` FOREIGN KEY (`Customer Id`) REFERENCES `Customers`(`Id`);

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk1` FOREIGN KEY (`Position Id`) REFERENCES `Position`(`Id`);

ALTER TABLE `CheckIn` ADD CONSTRAINT `CheckIn_fk0` FOREIGN KEY (`Position Id`) REFERENCES `Position`(`Id`);

ALTER TABLE `CheckIn` ADD CONSTRAINT `CheckIn_fk1` FOREIGN KEY (`Customers Id`) REFERENCES `Customers`(`Id`);

ALTER TABLE `CheckIn` ADD PRIMARY KEY (`Position Id`, `Customers Id`, `Arrival Date`);




ALTER TABLE `Booking` ADD `Underage` INT(10);
ALTER TABLE `Booking` ADD `Adult` INT(10);

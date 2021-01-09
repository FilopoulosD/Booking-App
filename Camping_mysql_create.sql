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
	`Booking Date` DATE,
	`Underage` INT(10),
	`Adult` INT(10),
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

CREATE TABLE `Checkin`(
    `Booking Id` INT(10),
	`Arrival Date` DATE NOT NULL,
	`Due date of departure` DATE NOT NULL,
	`Position Id` int(10),
	PRIMARY KEY (`Booking Id`,`Arrival Date`,`Position Id`)
);


ALTER TABLE `Customers` ADD CONSTRAINT `Customers_fk0` FOREIGN KEY (`ResId`) REFERENCES `Customers`(`Id`);

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk0` FOREIGN KEY (`Customer Id`) REFERENCES `Customers`(`Id`);

ALTER TABLE `Booking` ADD CONSTRAINT `Booking_fk1` FOREIGN KEY (`Position Id`) REFERENCES `Position`(`Id`);

ALTER TABLE `Checkin` ADD CONSTRAINT `CheckIn_fk0` FOREIGN KEY (`Position Id`) REFERENCES `Position`(`Id`);

ALTER TABLE `Checkin` ADD CONSTRAINT `CheckIn_fk1` FOREIGN KEY (`Booking Id`) REFERENCES `Booking`(`Id`);




INSERT INTO Customers VALUES(100012,'Κατερίνα Γεωργίου',NULL,'6981010101','1994-08-13','144477',9,0);
INSERT INTO Customers VALUES(100015,'Παυλος Ακριβος ',NULL,'6972222225','1990-04-28','134499',9,0);
INSERT INTO Customers VALUES(100016,'Φανης Χαχας ',NULL,'6972222226','1990-05-28','134489',9,0);
INSERT INTO Customers VALUES(100017,'Γωγω Μανεση ',NULL,'6972222255','1992-03-18','134479',9,0);
INSERT INTO Customers VALUES(100018,'Θανος Γεωργιου ',NULL,'6972232255','1991-03-18','135479',9,0);

INSERT INTO Position VALUES(01,'Parking',5,NULL,NULL,1);
INSERT INTO Position VALUES(02,'Parking',5,NULL,NULL,1);
INSERT INTO Position VALUES(03,'Parking',7,NULL,NULL,2);
INSERT INTO Position VALUES(04,'Parking',9,NULL,NULL,3);


INSERT INTO Booking VALUES(06,100012,01,'2021-01-25','2021-01-31',10,0,'Occupied','2020-12-18',0,0);
INSERT INTO Booking VALUES(07,100015,02,'2021-02-16','2021-03-10',10,0,'Occupied','2020-01-01',0,0);


INSERT INTO Booking VALUES(08,100016,02,'2021-03-16','2021-03-20',10,0,'2020-01-01',0,0);
INSERT INTO Booking VALUES(09,100017,02,'2021-02-08','2021-02-12',10,0,'2020-01-01',0,0);
INSERT INTO Booking VALUES(10,100018,01,'2021-02-08','2021-02-12',10,0,'2020-01-01',0,0);
INSERT INTO Booking VALUES(11,100018,03,'2021-02-08','2021-02-12',10,0,'2020-01-01',0,0);
INSERT INTO Booking VALUES(12,100012,02,'2021-03-25','2021-03-31',10,0,'2020-01-01',0,0);
INSERT INTO Booking VALUES(13,100015,01,'2021-04-08','2021-04-12',10,0,'2020-01-01',0,0);


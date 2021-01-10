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




INSERT INTO Customers VALUES(101,'Κατερίνα Γεωργίου',NULL,'6981010101','1994-08-13','144477',5,0);
INSERT INTO Customers VALUES(102,'Παυλος Ακριβος ',NULL,'6972222225','1990-04-28','134499',5,0);
INSERT INTO Customers VALUES(103,'Φανης Χαχας ',NULL,'6972222226','1990-05-28','134489',5,0);
INSERT INTO Customers VALUES(104,'Γωγω Μανεση ',NULL,'6972222255','1992-03-18','134479',5,0);
INSERT INTO Customers VALUES(105,'Θανος Παύλου ',NULL,'6972232255','1991-03-18','135479',5,0);
INSERT INTO Customers VALUES(106,'Γιώργος Δημητρίου',NULL,'698958888','1970-02-11','158877',5,0);
INSERT INTO Customers VALUES(107,'Σουλα Μάνεση',106,'69811122211','1975-06-07','143333',5,0);
INSERT INTO Customers VALUES(108,'Γιαννης Δημητρίου',106,NULL,'2010-12-09',NULL,3,0);
INSERT INTO Customers VALUES(109,'Φωτης Αλεξίου',NULL,'6912121212','1996-07-19','176666',5,0);
INSERT INTO Customers VALUES(110,'Χαρά Μητροπούλου',109,'6912121217','1998-07-13','175566',5,0);


INSERT INTO Position VALUES(01,'Parking',5,NULL,NULL,1);
INSERT INTO Position VALUES(02,'Parking',5,NULL,NULL,1);
INSERT INTO Position VALUES(03,'Parking',5,NULL,NULL,1);
INSERT INTO Position VALUES(04,'Tent',8,NULL,NULL,2);
INSERT INTO Position VALUES(05,'Tent',9,NULL,NULL,3);
INSERT INTO Position VALUES(06,'Tent',11,'YES','YES',5);
INSERT INTO Position VALUES(07,'Tent',8,'YES','YES',2);
INSERT INTO Position VALUES(08,'Tent',10,NULL,NULL,4);
INSERT INTO Position VALUES(09,'RV',15,'YES','YES',1);
INSERT INTO Position VALUES(10,'RV',15,NULL,NULL,1);



INSERT INTO Booking VALUES(606,101,04,'2021-01-25','2021-01-31',0,0,'2020-12-18',0,2);
INSERT INTO Booking VALUES(607,102,05,'2021-02-17','2021-03-10',0,0,'2020-12-19',0,3);
INSERT INTO Booking VALUES(608,103,04,'2021-01-12','2021-01-22',0,0,'2020-12-21',0,2);
INSERT INTO Booking VALUES(609,104,02,'2021-02-08','2021-02-12',0,0,'2020-12-23',0,0);
INSERT INTO Booking VALUES(610,104,06,'2021-02-08','2021-02-12',0,0,'2021-12-24',2,2);
INSERT INTO Booking VALUES(611,105,07,'2021-02-08','2021-02-12',0,0,'2020-12-27',0,2);
INSERT INTO Booking VALUES(612,106,05,'2021-01-10','2021-01-19',0,0,'2021-01-02',1,2);
INSERT INTO Booking VALUES(613,109,10,'2021-01-07','2021-01-14',0,0,'2020-01-03',0,2);

INSERT INTO Checkin VALUES(612,'2021-01-10','2021-01-19',05);
INSERT INTO Checkin VALUES(613,'2021-01-07','2021-01-14',10);

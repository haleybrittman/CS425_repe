CREATE SCHEMA `reserves` ;

CREATE TABLE `reserves`.`sailors` (
  `Sname` VARCHAR(10) NULL,
  `SID` INT NOT NULL,
  `Rating` INT NULL,
  `Age` INT NULL,
  PRIMARY KEY (`SID`));

INSERT INTO reserves.sailors (SID, Sname, Rating, Age) VALUES
(23, "Marx", 8, 52),
(25, "Martin", 9, 51),
(27, "Adams", 8, 36),
(33, "Carrey", 10, 22);

CREATE TABLE `reserves`.`boats` (
  `Bname` VARCHAR(15) NULL,
  `BID` INT NOT NULL,
  `Fee` DECIMAL(10,2) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`BID`));

INSERT INTO reserves.boats (BID, Bname, Fee, Location)  
VALUES (109, "Wayfarer", 120, "Hout Bay"), (108, "SeaPride", 500, "Fish Hoek"), (101, "Yuppie", 400, "Hout Bay"), (104, "Joy", 200, "Hout Bay");

CREATE TABLE `reserves`.`captains` (
  `Sname` VARCHAR(10) NULL,
  `SID` INT NOT NULL,
  `Rating` INT NULL,
  `Age` INT NULL,
  PRIMARY KEY (`SID`));

INSERT INTO reserves.captains (SID, Sname, Rating, Age) VALUES
(23, "Marx", 8, 52),
(25, "Martin", 9, 51),
(27, "Adams", 8, 36),
(33, "Carrey", 10, 22);

CREATE TABLE `reserves`.`reserves` (
  `SID` INT NOT NULL,
  `BID` INT NOT NULL,
  `Day` DATE NULL,
  `Deposit` DECIMAL(10,2) NULL,
  PRIMARY KEY (`SID`, `BID`),
  CONSTRAINT `SID`
    FOREIGN KEY (`SID`)
    REFERENCES `reserves`.`sailors` (`SID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `BID`
    FOREIGN KEY (`BID`)
    REFERENCES `reserves`.`boats` (`BID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO reserves.reserves (SID, BID, Day, Deposit)  
VALUES (23, 109, '2014-08-01', 120.00),
(23, 108, '2014-08-08', 120.00),
(25, 101, '2014-08-08', 0.00),
(27, 101, '2014-08-09', 100.00),
(27, 109, '2014-08-15', 120.00),
(33, 109, '2014-09-04', 0.00),
(33, 104, '2014-09-11', 0.00);
CREATE SCHEMA `boats` ;

CREATE TABLE `boats`.`boats` (
  `Bname` VARCHAR(15) NULL,
  `BID` INT NOT NULL,
  `Fee` DECIMAL(10,2) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`BID`));

INSERT INTO boats.boats (BID, Bname, Fee, Location)  
VALUES (109, "Wayfarer", 120, "Hout Bay"), (108, "SeaPride", 500, "Fish Hoek"), (101, "Yuppie", 400, "Hout Bay"), (104, "Joy", 200, "Hout Bay");

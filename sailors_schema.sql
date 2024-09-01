CREATE SCHEMA `sailors` ;
CREATE TABLE `sailors`.`sailors` (
  `Sname` VARCHAR(10) NULL,
  `SID` INT NOT NULL,
  `Rating` INT NULL,
  `Age` INT NULL,
  PRIMARY KEY (`SID`));

INSERT INTO sailors.sailors (SID, Sname, Rating, Age) VALUES
(23, "Marx", 8, 52),
(25, "Martin", 9, 51),
(27, "Adams", 8, 36),
(33, "Carrey", 10, 22);
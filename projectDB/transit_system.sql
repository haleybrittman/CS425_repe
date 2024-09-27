create database transit_system;
use transit_system;

create table Bus (
    Bus_ID int primary key,
    Bus_Type varchar(50),
    Wheelchair_accessibility boolean,
    Capacity INT
);

create table Bus_route (
    Route_no int primary key,
    name varchar(100),
    Direction varchar(10)
);

CREATE TABLE Train (
    Train_ID INT PRIMARY KEY,
    Capacity INT
);


CREATE TABLE Passenger (
    Passenger_ID INT PRIMARY KEY,
    Disabled BOOLEAN,
    Name VARCHAR(100),
    Phone_Number VARCHAR(15),
    Bus_ID INT,
    Train_ID INT,
    FOREIGN KEY (Bus_ID) REFERENCES Bus(Bus_ID),
    FOREIGN KEY (Train_ID) REFERENCES Train(Train_ID)
);

CREATE TABLE Line (
    ColorType VARCHAR(20),
    Name VARCHAR(100),
    Direction VARCHAR(10),
    Start VARCHAR(100),
    PRIMARY KEY (ColorType, Name, Direction)
);

CREATE INDEX idx_line_name ON Line(Name);



CREATE TABLE Train_stop (
    Time TIME,
    Station_Name VARCHAR(100),
    ETA TIME,
    Line_Name VARCHAR(100),
    PRIMARY KEY (Time, Station_Name, Line_Name),
    FOREIGN KEY (Line_Name) REFERENCES Line(Name)
);

CREATE TABLE Bus_Bus_route (
    Bus_ID INT,
    Route_no INT,
    PRIMARY KEY (Bus_ID, Route_no),
    FOREIGN KEY (Bus_ID) REFERENCES Bus(Bus_ID),
    FOREIGN KEY (Route_no) REFERENCES Bus_route(Route_no)
);
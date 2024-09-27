create database transit_system;
use transit_system;


-- Starting relations 
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
-- Bridge/ extra relations


-- Data inserts 
INSERT INTO Bus(bus_id,bus_type,Wheelchair_accessibility,Capacity)
Values 
(1,'Dodge',true,25), 
(2,'Plymouth',false,27),
(3,'Dodge',false,29),
(4,'Mercedes-Benz',true,22),
(5,'Mazda',false,28),
(6,'Toyota',false,27),
(7,'Ferrari',true,25),
(8,'Mazda',false,20),
(9,'Volkswagen',false,20),
(10,'Subaru',false,23),
(11,'Mercury',false,21),
(12,'Infiniti',true,27),
(13,'Volkswagen',true,22),
(14,'Mazda',false,29),
(15,'Chevrolet',false,30);

INSERT INTO train (Train_ID, Capacity)
VALUES 
(741690980, 62),
(093499398, 34),
(120224397, 61),
(725380068, 35),
(989894361, 100),
(343794754, 61),
(475798064, 90),
(214635394, 38),
(226444705, 78),
(714683592, 100),
(394853906, 17),
(411061933, 43),
(681525652, 18),
(669716397, 15),
(262316789, 43);

INSERT INTO line (ColorType, Name, Direction, Start)
VALUES 
('Teal', 'Al Dhafra Air Base', 'North', 'Pannier'),
('Khaki', 'Martubah Airport', 'South', 'Domainer'),
('Maroon', 'Sidney Municipal Airport', 'West', 'Transcof'),
('Fuscia', 'DLF Airport', 'East', 'Rank'),
('Orange', 'Donaldson Airport', 'North', 'Y-find'),
('Teal', 'Phoenix-Mesa-Gateway Airport', 'South', 'Bitchip'),
('Teal', 'Esler Regional Airport', 'East', 'Wrapsafe'),
('Puce', 'Garanhuns Airport', 'East', 'Flowdesk'),
('Violet', 'Kugaaruk Airport', 'West', 'Kanlam'),
('Yellow', 'Pelaneng Airport', 'East', 'Tin'),
('Aquamarine', 'Franco Bianco Airport', 'West', 'Zamit'),
('Purple', 'Nyagan Airport', 'South', 'Kanlam'),
('Puce', 'Gorgan Airport', 'East', 'Veribet'),
('Teal', 'Wevelgem Airport', 'East', 'Tempsoft'),
('Green', 'Plínio Alarcom Airport', 'North', 'Daltfresh');

INSERT INTO Passenger (Name, Passenger_ID, Disabled, Phone_Number, train_id, bus_id)
VALUES 
('Emlynn Cuerdall', 1, FALSE, '(816) 3133066', 741690980, 1),
('Irita Hamilton', 2, FALSE, '(922) 7203092', 093499398, 2),
('Briney Diggin', 3, FALSE, '(176) 8865626', 120224397, 3),
('Mair Macveigh', 4, FALSE, '(912) 7409457', 725380068, 4),
('Cece Pauler', 5, FALSE, '(127) 9045294', 989894361, 5),
('Evvie Etock', 6, FALSE, '(937) 9611365', 343794754, 6),
('Jennie Cockney', 7, TRUE, '(186) 2525643', 475798064, 7),
('Neila Jutson', 8, TRUE, '(185) 7435586', 214635394, 8),
('Lotta Glusby', 9, FALSE, '(237) 2792749', 226444705, 9),
('Timotheus Barnsdall', 10, FALSE, '(861) 5822530', 714683592, 10),
('Babette Dye', 11, FALSE, '(148) 2303911', 394853906, 11),
('Neel Semmens', 12, TRUE, '(996) 6810235', 411061933, 12),
('Vivi Philipps', 13, TRUE, '(255) 5456390', 681525652, 13),
('Robenia Markham', 14, FALSE, '(750) 7803496', 669716397, 14),
('Humberto Foxwell', 15, TRUE, '(276) 7872569', 262316789, 15);
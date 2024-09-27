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
    Station_Name VARCHAR(100),
    Line_Name VARCHAR(100),
    PRIMARY KEY (Station_Name, Line_Name),
    FOREIGN KEY (Line_Name) REFERENCES Line(Name)
);




CREATE TABLE Bus_stops (
    Stop_Name VARCHAR(30),
    Route INT,
    Stop_Order INT,
    PRIMARY KEY (Stop_Name, Route),
    FOREIGN KEY (Route) REFERENCES bus_route(route_no)
);

-- Bridge/ extra relations

CREATE TABLE Bus_Bus_route (
    Bus_ID INT,
    Route_no INT,
    PRIMARY KEY (Bus_ID, Route_no),
    FOREIGN KEY (Bus_ID) REFERENCES Bus(Bus_ID),
    FOREIGN KEY (Route_no) REFERENCES Bus_route(Route_no)
);

CREATE TABLE Train_Line (
    Train_ID int,
    ColorType VARCHAR(15),
    Name VARCHAR(30),
    Direction VARCHAR(7),
    PRIMARY KEY (Train_ID, ColorType, Name, Direction)
);

CREATE TABLE Line_Train_Stops (
    ColorType VARCHAR(15),
    Name VARCHAR(30),
    Direction VARCHAR(7),
    Station_Name VARCHAR(30),
    PRIMARY KEY (ColorType, Name, Direction, Station_Name)
);

CREATE TABLE Bus_Route_Bus_Stops (
    Stop_name VARCHAR(30),
    Route_no INT,
    PRIMARY KEY (Stop_name, Route_no),
    FOREIGN KEY (Stop_name) REFERENCES Bus_stops(stop_Name),
    FOREIGN KEY (Route_no) REFERENCES Bus_route(route_no)
);


CREATE TABLE Bus_Stops_Time (
    Stop_Name VARCHAR(30),
    Route INT,
    Time TIME,
    ETA TIME,
    PRIMARY KEY (Stop_Name, Route, Time),
    FOREIGN KEY (Stop_Name, Route) REFERENCES Bus_stops(Stop_Name, Route)
);


CREATE TABLE Bus_Stops_Stop_Order (
    Stop_Name VARCHAR(30),
    Location VARCHAR(30),
    Route INT,
    Stop_Order INT,
    PRIMARY KEY (stop_name, Location, Route),
    FOREIGN KEY (stop_name, Route) REFERENCES bus_stops(stop_name, route)
);


CREATE TABLE Train_Stops_Time (
    TID int,
    Station_Name VARCHAR(100),
    Line_Name VARCHAR(100),
    Time TIME,
    PRIMARY KEY (TID, Station_Name, Line_Name, Time),
    FOREIGN KEY (Station_Name, Line_Name) REFERENCES Train_stop(Station_Name, Line_Name)
);


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

INSERT INTO bus_route (route_no, name, direction) VALUES
(1, 'Route A', 'East'),
(2, 'Route A', 'West'),
(3, 'Route C', 'West'),
(4, 'Route E', 'West'),
(5, 'Route E', 'North'),
(6, 'Route C', 'West'),
(7, 'Route E', 'South'),
(8, 'Route D', 'South'),
(9, 'Route A', 'South'),
(10, 'Route B', 'West'),
(11, 'Route A', 'West'),
(12, 'Route C', 'North'),
(13, 'Route E', 'South'),
(14, 'Route D', 'West'),
(15, 'Route E', 'East');

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

INSERT INTO Bus_Bus_route (Bus_ID, Route_no) VALUES
(1, 8),
(2, 3),
(3, 12),
(4, 5),
(5, 15),
(6, 1),
(7, 10),
(8, 7),
(9, 14),
(10, 2),
(11, 9),
(12, 6),
(13, 11),
(14, 4),
(15, 13);



INSERT INTO Bus_stops (Stop_Name, Route, Stop_Order) VALUES
('Stop1', 1, 1),
('Stop2', 2, 2),
('Stop3', 3, 3),
('Stop4', 4, 4),
('Stop5', 5, 5),
('Stop6', 6, 6),
('Stop7', 7, 7),
('Stop8', 8, 8),
('Stop9', 9, 9),
('Stop10', 10, 10),
('Stop11', 11, 11),
('Stop12', 12, 12),
('Stop13', 13, 13),
('Stop14', 14, 14),
('Stop15', 15, 15);


INSERT INTO Bus_Stops_Time (Stop_Name, Route, Time, ETA) VALUES
('Stop1', 1, '08:00:00', ADDTIME('08:00:00', '00:05:00')),
('Stop2', 2, '08:10:00', ADDTIME('08:10:00', '00:05:00')),
('Stop3', 3, '08:20:00', ADDTIME('08:20:00', '00:05:00')),
('Stop4', 4, '08:30:00', ADDTIME('08:30:00', '00:05:00')),
('Stop5', 5, '08:40:00', ADDTIME('08:40:00', '00:05:00')),
('Stop6', 6, '08:50:00', ADDTIME('08:50:00', '00:05:00')),
('Stop7', 7, '09:00:00', ADDTIME('09:00:00', '00:05:00')),
('Stop8', 8, '09:10:00', ADDTIME('09:10:00', '00:05:00')),
('Stop9', 9, '09:20:00', ADDTIME('09:20:00', '00:05:00')),
('Stop10', 10, '09:30:00', ADDTIME('09:30:00', '00:05:00')),
('Stop11', 11, '09:40:00', ADDTIME('09:40:00', '00:05:00')),
('Stop12', 12, '09:50:00', ADDTIME('09:50:00', '00:05:00')),
('Stop13', 13, '10:00:00', ADDTIME('10:00:00', '00:05:00')),
('Stop14', 14, '10:10:00', ADDTIME('10:10:00', '00:05:00')),
('Stop15', 15, '10:20:00', ADDTIME('10:20:00', '00:05:00'));

INSERT INTO Bus_Stops_Stop_Order (Stop_Name, Location, Route, Stop_Order) VALUES
('Stop1', 'LocationA', 1, 3),
('Stop2', 'LocationB', 2, 7),
('Stop3', 'LocationC', 3, 1),
('Stop4', 'LocationD', 4, 9),
('Stop5', 'LocationE', 5, 2),
('Stop6', 'LocationF', 6, 6),
('Stop7', 'LocationG', 7, 4),
('Stop8', 'LocationH', 8, 10),
('Stop9', 'LocationI', 9, 5),
('Stop10', 'LocationJ', 10, 8),
('Stop11', 'LocationK', 11, 11),
('Stop12', 'LocationL', 12, 12),
('Stop13', 'LocationM', 13, 13),
('Stop14', 'LocationN', 14, 14),
('Stop15', 'LocationO', 15, 15);

INSERT INTO Bus_Route_Bus_Stops (Stop_name, Route_no) VALUES
('Stop1', 1),
('Stop2', 2),
('Stop3', 3),
('Stop4', 4),
('Stop5', 5),
('Stop6', 6),
('Stop7', 7),
('Stop8', 8),
('Stop9', 9),
('Stop10', 10),
('Stop11', 11),
('Stop12', 12),
('Stop13', 13),
('Stop14', 14),
('Stop15', 15);

INSERT INTO Train_stop (Station_Name, Line_Name) VALUES
('Station 1', 'Franco Bianco Airport'),
('Station 2', 'DLF Airport'),
('Station 3', 'Plínio Alarcom Airport'),
('Station 4', 'Martubah Airport'),
('Station 5', 'Sidney Municipal Airport'),
('Station 6', 'Donaldson Airport'),
('Station 7', 'Garanhuns Airport'),
('Station 8', 'Gorgan Airport'),
('Station 9', 'Nyagan Airport'),
('Station 10', 'Al Dhafra Air Base'),
('Station 11', 'Esler Regional Airport'),
('Station 12', 'Phoenix-Mesa-Gateway Airport'),
('Station 13', 'Wevelgem Airport'),
('Station 14', 'Kugaaruk Airport'),
('Station 15', 'Pelaneng Airport');


INSERT INTO Train_Stops_Time (TID, Station_Name, Line_Name, Time) VALUES
(1, 'Station 1', 'Franco Bianco Airport', '08:00:00'),
(2, 'Station 2', 'DLF Airport', '08:15:00'),
(3, 'Station 3', 'Plínio Alarcom Airport', '08:30:00'),
(4, 'Station 4', 'Martubah Airport', '08:45:00'),
(5, 'Station 5', 'Sidney Municipal Airport', '09:00:00'),
(6, 'Station 6', 'Donaldson Airport', '09:15:00'),
(7, 'Station 7', 'Garanhuns Airport', '09:30:00'),
(8, 'Station 8', 'Gorgan Airport', '09:45:00'),
(9, 'Station 9', 'Nyagan Airport', '10:00:00'),
(10, 'Station 10', 'Al Dhafra Air Base', '10:15:00'),
(11, 'Station 11', 'Esler Regional Airport', '10:30:00'),
(12, 'Station 12', 'Phoenix-Mesa-Gateway Airport', '10:45:00'),
(13, 'Station 13', 'Wevelgem Airport', '11:00:00'),
(14, 'Station 14', 'Kugaaruk Airport', '11:15:00'),
(15, 'Station 15', 'Pelaneng Airport', '11:30:00');

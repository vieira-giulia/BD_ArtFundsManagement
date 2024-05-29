-- CREATE DATABASE
DROP TABLE IF EXISTS 'Objects';
DROP TABLE IF EXISTS 'Artists';
DROP TABLE IF EXISTS 'Users';
DROP TABLE IF EXISTS 'Logs';

-- Table 01: Artistic Object
CREATE TABLE Objects (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Theme VARCHAR(255),
    Genre VARCHAR(255),
    Year VARCHAR(4),
    TypeArt VARCHAR(255),
    Material VARCHAR(255),
    AuthorID INT NOT NULL,
    ExecutorID INT NOT NULL,
    Owner VARCHAR(255),
    FOREIGN KEY (AuthorID) REFERENCES Artists(ID),
    FOREIGN KEY (ExecutorID) REFERENCES Artists(ID)
);

-- Table 02: Artists
CREATE TABLE Artists (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    DateInit DATE,
    DateEnd DATE
);

-- Table 03: Users
CREATE TABLE Users (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255)
);

-- Table 04: Logs
CREATE TABLE Logs (
    Date TIMESTAMP PRIMARY KEY,
    ObjectID INT NOT NULL,
    ArtistID INT NOT NULL,
    FOREIGN KEY (ObjectID) REFERENCES ArtisticObject(ID),
    FOREIGN KEY (ArtistID) REFERENCES Artists(ID)
);



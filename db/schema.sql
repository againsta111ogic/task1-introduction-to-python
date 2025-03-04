CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS rooms(
    id INT,
    name VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS students(
    birthday DATETIME(6) NOT NULL,
    id INT,
    name VARCHAR(255) NOT NULL,
    room INT,
    sex CHAR(1) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (room) REFERENCES rooms (id)
);


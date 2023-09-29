-- SQLBook: Code
DROP DATABASE IF EXISTS escuela;

CREATE DATABASE escuela CHARACTER SET utf8mb4;

USE escuela;

CREATE TABLE alumnos (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
apellido1 VARCHAR(100) NOT NULL,
apellido2 VARCHAR(100),
curso VARCHAR(100),
turno VARCHAR(100)
);

CREATE TABLE asistencia (
        fecha VARCHAR(100),
        presentismo VARCHAR(255),
        idAlumno INT UNSIGNED,
        FOREIGN KEY (idAlumno) REFERENCES alumnos (id) ON DELETE CASCADE
    );


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
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  fecha date,
  presentismo enum('Presente','Tarde','Ausente'),
  idAlumno INT UNSIGNED NOT NULL,
  foreign key (idAlumno) references alumnos(id)
);

INSERT INTO alumnos VALUES(1,'Juan Cruz','Cetro',NULL,'4°2°','Manana');
INSERT INTO asistencia VALUES(1,'2023-08-18','Presente',1);
INSERT INTO alumnos VALUES(2,'Roman','Abalos','Ishida','4°2°','Manana');
INSERT INTO asistencia VALUES(2,'2023-08-18','Tarde',2);

SELECT * from alumnos
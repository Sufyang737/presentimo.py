-- SQLBook: Code
-- Active: 1692762019367@@127.0.0.1@3306@escoela
DROP DATABASE IF EXISTS escoela;
CREATE DATABASE escoela CHARACTER SET utf8mb4;
USE escoela;

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
--delimiter $$
--drop trigger if exists agregar_fecha$$

--create trigger agregar_fecha
--before insert 
--on asistencia for each row 
--begin 
   --set NEW.fecha = now() ;

--end $$

--delimiter ;

INSERT INTO alumnos VALUES(1,'Juan Cruz','Cetro',NULL,'4°2°','Mañana');
INSERT INTO asistencia VALUES(1,'2023-08-18','Presente',1);
INSERT INTO alumnos VALUES(2,'Roman','Abalos','Ishida','4°2°','Mañana');
INSERT INTO asistencia VALUES(2,'2023-08-18','Tarde',2);
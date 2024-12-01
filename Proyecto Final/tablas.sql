CREATE DATABASE IF NOT EXISTS sistema_hospital;
USE sistema_hospital;

CREATE TABLE Pacientes (
    paciente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(10) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    direccion VARCHAR(200) NOT NULL,
    obra_social VARCHAR (200) NOT NULL
);

CREATE TABLE Medicos (
    medico_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    matricula VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL UNIQUE,
    especialidad VARCHAR(100) NOT NULL
);

CREATE TABLE Turnos (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(paciente_id) ON DELETE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES Medicos(medico_id) ON DELETE CASCADE
);

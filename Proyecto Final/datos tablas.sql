INSERT INTO Pacientes (nombre, apellido, dni, telefono, email, direccion, obra_social) VALUES
('Franco', 'Juarez', '29519200', '123456789', 'fran.madrugador@mail.com', 'La Frontera 123', 'OSDE'),
('Lucía', 'Canclini', '27619201', '987654321', 'lu.chica100@mail.com', 'Avenida La Niñera 456', 'Swiss Medical'),
('Santiago', 'Castellaro', '26619202', '555123456', 'caste.perezlover@mail.com', 'Calle Vitadini 789', 'OSECAC'),
('Rodrigo', 'Alvarez', '28919203', '666777888', 'rodri.vejestorio@mail.com', 'Cuarentón Inmadurez 987', 'PAMI'),
('Sofía', 'Hernández', '30719204', '123123123', 'sofia.hernandez@mail.com', 'Calle Tercera 101', 'OMINT'),
('Luis', 'Rodríguez', '25819205', '456456456', 'luis.rodriguez@mail.com', 'Calle Cuarta 202', 'Medifé'),
('María', 'Sánchez', '24119206', '789789789', 'maria.sanchez@mail.com', 'Calle Quinta 303', 'OSDE'),
('Pedro', 'Fernández', '28200207', '321321321', 'pedro.fernandez@mail.com', 'Calle Sexta 404', 'Swiss Medical'),
('Julia', 'Jiménez', '28500208', '654654654', 'julia.jimenez@mail.com', 'Calle Séptima 505', 'PAMI'),
('Miguel', 'Ruiz', '27900209', '987987987', 'miguel.ruiz@mail.com', 'Calle Octava 606', 'Galeno');

INSERT INTO Medicos (nombre, apellido, matricula, telefono, especialidad) VALUES
('Dr. Javier', 'Torres', '11122', '111222334', 'Cardiología'),
('Dra. Marta', 'Vega', '33344', '222333444', 'Neurología'),
('Dr. Pablo', 'García', '44455', '333444555', 'Pediatría'),
('Dra. Claudia', 'Pérez', '55666', '444555666', 'Ginecología'),
('Dr. Diego', 'Gómez', '67774', '555666777', 'Dermatología'),
('Dr. Sergio', 'Martínez', '18999', '666777888', 'Traumatología'),
('Dra. Teresa', 'Hernández', '78834', '777888999', 'Oftalmología'),
('Dr. Andrés', 'López', '12223', '888999111', 'Psiquiatría'),
('Dra. Elena', 'Rodríguez', '22234', '999111222', 'Otorrinolaringología'),
('Dr. Alberto', 'Sánchez', '99914', '111222333', 'Urología');

INSERT INTO Turnos (id_paciente, id_medico, fecha, hora) VALUES
(1, 1, '2024-12-01', '09:00:00'),
(2, 2, '2024-12-01', '10:00:00'),
(3, 3, '2024-12-01', '11:00:00'),
(4, 4, '2024-12-02', '09:30:00'),
(5, 5, '2024-12-02', '10:30:00'),
(6, 6, '2024-12-02', '11:30:00'),
(7, 7, '2024-12-03', '09:00:00'),
(8, 8, '2024-12-03', '10:00:00'),
(9, 9, '2024-12-03', '11:00:00'),
(10, 10, '2024-12-04', '09:30:00');
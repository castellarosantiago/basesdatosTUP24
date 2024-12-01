-- PROCEDIMIENTO PARA PROGRAMAR UN TURNO

DELIMITER //

CREATE PROCEDURE programar_turno(
    IN t_paciente_id INT,
    IN t_medico_id INT,
    IN t_fecha DATE,
    IN t_hora TIME
)
BEGIN
    -- Verificar si el médico está disponible
    IF NOT EXISTS (
        SELECT 1
        FROM Turnos
        WHERE id_medico = t_medico_id
        AND fecha = t_fecha
        AND hora = t_hora
    ) THEN
        -- Si está disponible, insertar el turno
        INSERT INTO Turnos (id_paciente, id_medico, fecha, hora)
        VALUES (t_paciente_id, t_medico_id, t_fecha, t_hora);
    ELSE
        -- Si no está disponible, generar un error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El médico no está disponible en esa fecha y hora';
    END IF;
END //

DELIMITER ;


-- PROCEDIMIENTO PARA CANCELAR UN TURNO

DELIMITER //

CREATE PROCEDURE cancelar_turno(
    IN t_id_turno INT
)
BEGIN
    -- Verificar si el turno existe
    IF EXISTS (
        SELECT 1
        FROM Turnos
        WHERE id_turno = t_id_turno
    ) THEN
        -- Eliminar el turno
        DELETE FROM Turnos
        WHERE id_turno = t_id_turno;
    ELSE
        -- Si no existe, generar un error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El turno especificado no existe';
    END IF;
END //

DELIMITER ;


-- PROCEDIMIENTO PARA CANCELAR SEGÚN ID DE MÉDICO Y RANGO DE FECHA

DELIMITER //

CREATE PROCEDURE `cancelar_turnos_por_medico_y_fecha`(
    IN t_medico_id INT,
    IN t_fecha_inicio DATE,
    IN t_fecha_fin DATE
)
BEGIN
    -- Verificar si hay turnos que coincidan con los parámetros
    IF EXISTS (
        SELECT 1
        FROM Turnos
        WHERE id_medico = t_medico_id
        AND fecha BETWEEN t_fecha_inicio AND t_fecha_fin
    ) THEN
        -- Eliminar los turnos que coincidan
        DELETE FROM Turnos
        WHERE id_medico = t_medico_id
        AND fecha BETWEEN t_fecha_inicio AND t_fecha_fin;
    ELSE
        -- Si no hay turnos, generar un mensaje de error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No existen turnos para cancelar con los parámetros especificados';
    END IF;
END
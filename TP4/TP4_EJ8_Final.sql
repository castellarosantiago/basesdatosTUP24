--Ejercicio 8: Sincronización de Base de Datos

CREATE TABLE InventarioLocal (
    ProductoId INT PRIMARY KEY IDENTITY(1,1),
    NombreProducto VARCHAR(100) NOT NULL,
    Cantidad INT NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    UltimaActualizacion DATETIME NOT NULL
);

-- En Base de Datos Remota
CREATE TABLE InventarioRemoto (
    ProductoId INT PRIMARY KEY IDENTITY(1,1),
    NombreProducto VARCHAR(100) NOT NULL,
    Cantidad INT NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    UltimaActualizacion DATETIME NOT NULL
);



-- Datos de ejemplo para InventarioLocal
INSERT INTO InventarioLocal (NombreProducto, Cantidad, Precio, UltimaActualizacion)
VALUES 
    ('Producto A', 10, 100.50, '2024-10-25 10:30:00'),
    ('Producto B', 5, 200.00, '2024-10-25 11:00:00'),
    ('Producto C', 15, 75.75, '2024-10-25 09:45:00'),
    ('Producto D', 8, 150.25, '2024-10-25 14:20:00'),
    ('Producto E', 20, 50.00, '2024-10-25 13:10:00');

-- Datos de ejemplo para InventarioRemoto
INSERT INTO InventarioRemoto (NombreProducto, Cantidad, Precio, UltimaActualizacion)
VALUES 
    ('Producto F', 12, 120.00, '2024-10-25 10:45:00'),
    ('Producto G', 9, 180.30, '2024-10-25 12:15:00'),
    ('Producto H', 6, 90.40, '2024-10-25 08:55:00'),
    ('Producto I', 3, 250.00, '2024-10-25 15:30:00'),
    ('Producto J', 11, 60.60, '2024-10-25 10:05:00');



--Objetivo: Crear un procedimiento almacenado llamado SincronizarInventario en la base de datos local que utilice un cursor para comparar y sincronizar los registros de InventarioLocal con InventarioRemoto.

CREATE DEFINER=`root`@`localhost` PROCEDURE `SincronizarInventario`()
BEGIN
    DECLARE v_ProductoId INT;
    DECLARE v_NombreProducto VARCHAR(100) DEFAULT "";
    DECLARE v_Cantidad INT DEFAULT 0;
    DECLARE v_Precio DECIMAL(10,2) DEFAULT 0;
    DECLARE v_UltimaActualizacion DATETIME DEFAULT now();
    DECLARE done BOOL DEFAULT FALSE;

    DECLARE cursor_inventarioLocal CURSOR FOR
        SELECT ProductoId, NombreProducto, Cantidad, Precio, UltimaActualizacion
        FROM InventarioLocal;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursor_inventarioLocal;

    FETCH cursor_inventarioLocal INTO v_ProductoId, v_NombreProducto, v_Cantidad, v_Precio, v_UltimaActualizacion;
    
    WHILE NOT done DO
        IF EXISTS (SELECT 1 FROM InventarioRemoto WHERE ProductoId = v_ProductoId OR UltimaActualizacion <> v_UltimaActualizacion) THEN
            UPDATE InventarioRemoto
            SET `NombreProducto` = v_NombreProducto,
                `Cantidad` = v_Cantidad,
                `Precio` = v_Precio,
                `UltimaActualizacion` = v_UltimaActualizacion
            WHERE `ProductoId` = v_ProductoId;
        ELSE
			INSERT INTO InventarioRemoto (`ProductoId`, `NombreProducto`, `Cantidad`, `Precio`, `UltimaActualizacion`)
			VALUES (v_ProductoId, v_NombreProducto, v_Cantidad, v_Precio, v_UltimaActualizacion);
        END IF;

        FETCH cursor_inventarioLocal INTO v_ProductoId, v_NombreProducto, v_Cantidad, v_Precio, v_UltimaActualizacion;
    END WHILE;

    CLOSE cursor_inventarioLocal;
END
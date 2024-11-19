DELIMETER //
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
END//
DELIMETER ;
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
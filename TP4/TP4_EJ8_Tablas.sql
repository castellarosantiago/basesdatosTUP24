-- Base de Datos Local

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
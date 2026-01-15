CREATE DATABASE IF NOT EXISTS ciber;
USE ciber;
CREATE TABLE ropa(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
    talla VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    foto VARCHAR(255)
);
CREATE TABLE comentarios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`) VALUES ('root','1234', 'admin');

-- Insertamos 3 prendas de ejemplo
INSERT INTO `ropa` (`nombre`, `descripcion`, `precio`, `talla`, `color`, `categoria`, `foto`)
VALUES 
('Camiseta Urbana', 'Camiseta de algodón con estampado moderno', 19.99, 'M', 'Negro', 'Camisetas', 'https://via.placeholder.com/70x70.png?text=Camiseta'),
('Pantalón Vaquero', 'Jeans ajustados de corte moderno', 49.99, 'L', 'Azul', 'Pantalones', 'https://via.placeholder.com/70x70.png?text=Pantalon'),
('Chaqueta Deportiva', 'Chaqueta ligera para deporte', 79.99, 'S', 'Gris', 'Chaquetas', 'https://via.placeholder.com/70x70.png?text=Chaqueta');
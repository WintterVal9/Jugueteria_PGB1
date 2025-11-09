-- =============================================
-- AGREGAR MÁS DATOS PARA MÓDULO DE VENTAS
-- =============================================

INSERT INTO Producto (Nombre, Descripcion, Fecha_Vencimiento, Cantidad, Valor_Unitario, Id_Linea) VALUES
('Puzzle 1000 Piezas', 'Puzzle educativo para todas las edades', '2030-12-31', 25, 45000, 1),
('Tablet Infantil', 'Tablet con juegos educativos', '2026-08-15', 15, 180000, 2),
('Action Man', 'Figura de acción articulada', '2032-03-20', 35, 75000, 3),
('Monopoly Clásico', 'Juego de mesa familiar', '2034-11-30', 30, 85000, 4),
('Pista de Carreras', 'Pista con 2 carros de control remoto', '2031-07-10', 20, 120000, 5);

INSERT INTO Cliente (Nombre, Fecha_Nacimiento, Historial_Compras) VALUES
('Sofia Ramirez', '2001-04-18', 'Cliente nuevo primera compra'),
('Javier Mendoza', '1998-12-03', 'Prefiere juguetes electrónicos'),
('Catalina Rojas', '1992-07-29', 'Compra frecuente educativos'),
('Andres Silva', '1985-09-14', 'Cliente corporativo regalos');

INSERT INTO Venta (Descripcion, Valor_Total) VALUES
('Venta juguetes educativos premium', 385000),
('Venta electrónicos temporada navideña', 620000),
('Venta muñecas y accesorios boutique', 275000),
('Venta juegos de mesa familiares', 195000),
('Venta vehículos coleccionables', 340000),
('Venta promocional fin de mes', 280000),
('Venta cliente frecuente descuento', 450000),
('Venta mayorista productos varios', 890000);

INSERT INTO Detalle_Venta (Id_Venta, Id_Producto, Cantidad_Producto) VALUES
(6, 1, 2),  -- Venta 6: 2 Lego Classic
(6, 6, 1),  -- Venta 6: 1 Puzzle
(7, 2, 1),  -- Venta 7: 1 Robot
(7, 7, 2),  -- Venta 7: 2 Tablet
(8, 3, 3),  -- Venta 8: 3 Barbie
(8, 8, 1),  -- Venta 8: 1 Action Man
(9, 4, 2),  -- Venta 9: 2 Ajedrez
(9, 9, 1),  -- Venta 9: 1 Monopoly
(10, 5, 3), -- Venta 10: 3 Carro Bomberos
(10, 10, 2), -- Venta 10: 2 Pista Carreras
(11, 6, 1), -- Venta 11: 1 Puzzle
(11, 7, 1), -- Venta 11: 1 Tablet
(12, 8, 2), -- Venta 12: 2 Action Man
(12, 9, 1), -- Venta 12: 1 Monopoly
(13, 1, 4), -- Venta 13: 4 Lego
(13, 2, 1); -- Venta 13: 1 Robot


INSERT INTO Compra (Id_Cliente, Id_Producto) VALUES
(6, 1), (6, 6),
(7, 2), (7, 7),
(8, 3), (8, 8),
(9, 4), (9, 9);

-- =============================================
-- VERIFICAR DATOS 

-- =============================================

SELECT 'PRODUCTOS' as Tabla;
SELECT Id_Producto, Nombre, Cantidad, Valor_Unitario FROM Producto;

SELECT 'CLIENTES' as Tabla;  
SELECT Id_Cliente, Nombre FROM Cliente;

SELECT 'VENTAS' as Tabla;
SELECT Id_Venta, Descripcion, Valor_Total FROM Venta;

SELECT 'DETALLES VENTA' as Tabla;
SELECT dv.Id_Venta, p.Nombre as Producto, dv.Cantidad_Producto, p.Valor_Unitario
FROM Detalle_Venta dv
JOIN Producto p ON dv.Id_Producto = p.Id_Producto
ORDER BY dv.Id_Venta;

SELECT 'ESTADÍSTICAS VENTAS' as Reporte;
SELECT 
    COUNT(*) as Total_Ventas,
    SUM(Valor_Total) as Valor_Total_Ventas,
    AVG(Valor_Total) as Promedio_Venta
FROM Venta;

SELECT 'PRODUCTOS MÁS VENDIDOS' as Ranking;
SELECT 
    p.Nombre as Producto,
    SUM(dv.Cantidad_Producto) as Total_Vendido,
    SUM(dv.Cantidad_Producto * p.Valor_Unitario) as Valor_Total
FROM Detalle_Venta dv
JOIN Producto p ON dv.Id_Producto = p.Id_Producto
GROUP BY p.Id_Producto
ORDER BY Total_Vendido DESC;
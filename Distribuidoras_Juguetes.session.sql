-- =============================================
-- DATOS COMPLETOS PARA MÓDULO DE VENTAS
-- =============================================

-- 1. AGREGAR MÁS PRODUCTOS
INSERT INTO Producto (Nombre, Descripcion, Fecha_Vencimiento, Cantidad, Valor_Unitario, Id_Linea) VALUES
('Puzzle 1000 Piezas', 'Puzzle educativo para todas las edades', '2030-12-31', 25, 45000, 1),
('Tablet Infantil', 'Tablet con juegos educativos', '2026-08-15', 15, 180000, 2),
('Action Man', 'Figura de acción articulada', '2032-03-20', 35, 75000, 3),
('Monopoly Clásico', 'Juego de mesa familiar', '2034-11-30', 30, 85000, 4),
('Pista de Carreras', 'Pista con 2 carros de control remoto', '2031-07-10', 20, 120000, 5),
('Microscopio Infantil', 'Microscopio para pequeños científicos', '2029-05-25', 18, 95000, 1),
('Drone Control Remoto', 'Drone con cámara para niños mayores', '2025-12-15', 12, 300000, 2),
('Set de Muñecas Bebés', 'Set de 3 muñecas bebé con accesorios', '2033-02-SELECT Id_Producto, Nombre, Cantidad, Valor_Unitario 
FROM Producto 
ORDER BY Id_Producto;14', 40, 60000, 3),
('Uno Cards', 'Juego de cartas familiar colorido', '2035-01-01', 50, 25000, 4),
('Camión de Volteo', 'Camión de construcción grande', '2032-10-05', 28, 55000, 5);

-- 2. AGREGAR MÁS CLIENTES
INSERT INTO Cliente (Nombre, Fecha_Nacimiento, Historial_Compras) VALUES
('Sofía Ramírez', '2001-04-18', 'Cliente nuevo primera compra'),
('Javier Mendoza', '1998-12-03', 'Prefiere juguetes electrónicos'),
('Catalina Rojas', '1992-07-29', 'Compra frecuente educativos'),
('Andres Silva', '1985-09-14', 'Cliente corporativo regalos'),
('Daniela Castro', '1997-01-22', 'Interesada en juguetes de colección'),
('Ricardo Ortega', '1991-11-08', 'Compra para hijos pequeños'),
('Patricia Narvaez', '1988-06-17', 'Cliente premium con descuentos'),
('Fernando Gutierrez', '1994-03-25', 'Prefiere juegos de mesa familiares');

-- 3. AGREGAR VENTAS ADICIONALES
INSERT INTO Venta (Descripcion, Valor_Total) VALUES
('Venta juguetes educativos premium', 385000),
('Venta electrónicos temporada navideña', 620800),
('Venta muñecas y accesorios boutique', 275000),
('Venta juegos de mesa familiares', 195000),
('Venta vehículos coleccionables', 340000),
('Venta promocional fin de mes', 280000),
('Venta cliente frecuente descuento', 450000),
('Venta mayorista productos varios', 890000),
('Venta escolar material educativo', 320000),
('Venta cumpleaños infantil', 185000),
('Venta regalos corporativos', 760000),
('Venta temporada vacaciones', 420000);

-- 4. AGREGAR DETALLES DE VENTA
INSERT INTO Detalle_Venta (Id_Venta, Id_Producto, Cantidad_Producto) VALUES
-- Venta 6 (ID después de los 5 existentes)
(6, 1, 2),   -- 2 Lego Classic
(6, 6, 1),   -- 1 Puzzle
(6, 11, 1),  -- 1 Microscopio

-- Venta 7
(7, 2, 1),   -- 1 Robot
(7, 7, 2),   -- 2 Tablet
(7, 12, 1),  -- 1 Drone

-- Venta 8
(8, 3, 3),   -- 3 Barbie
(8, 8, 1),   -- 1 Action Man
(8, 13, 2),  -- 2 Set Muñecas

-- Venta 9
(9, 4, 2),   -- 2 Ajedrez
(9, 9, 1),   -- 1 Monopoly
(9, 14, 3),  -- 3 Uno Cards

-- Venta 10
(10, 5, 3),  -- 3 Carro Bomberos
(10, 10, 2), -- 2 Pista Carreras
(10, 15, 1), -- 1 Camión Volteo

-- Venta 11
(11, 6, 1),  -- 1 Puzzle
(11, 11, 2), -- 2 Microscopio

-- Venta 12
(12, 7, 1),  -- 1 Tablet
(12, 12, 1), -- 1 Drone

-- Venta 13
(13, 8, 2),  -- 2 Action Man
(13, 13, 1), -- 1 Set Muñecas

-- Venta 14
(14, 9, 1),  -- 1 Monopoly
(14, 14, 4), -- 4 Uno Cards

-- Venta 15
(15, 10, 2), -- 2 Pista Carreras
(15, 15, 3), -- 3 Camión Volteo

-- Venta 16
(16, 1, 1),  -- 1 Lego
(16, 2, 1),  -- 1 Robot
(16, 3, 1),  -- 1 Barbie
(16, 4, 1),  -- 1 Ajedrez
(16, 5, 1);  -- 1 Carro Bomberos

-- 5. AGREGAR REGISTROS DE COMPRA
INSERT INTO Compra (Id_Cliente, Id_Producto) VALUES
(6, 1), (6, 6), (6, 11),
(7, 2), (7, 7), (7, 12),
(8, 3), (8, 8), (8, 13),
(9, 4), (9, 9), (9, 14),
(10, 5), (10, 10), (10, 15),
(11, 6), (11, 11),
(12, 1), (12, 2), (12, 3),
(13, 4), (13, 5), (13, 6);

-- =============================================
-- VERIFICAR DATOS INSERTADOS
-- =============================================

-- Verificar conteos
SELECT 'RESUMEN DE DATOS' as Reporte;
SELECT 
    (SELECT COUNT(*) FROM Producto) as Total_Productos,
    (SELECT COUNT(*) FROM Cliente) as Total_Clientes,
    (SELECT COUNT(*) FROM Venta) as Total_Ventas,
    (SELECT COUNT(*) FROM Detalle_Venta) as Total_Detalles,
    (SELECT COUNT(*) FROM Compra) as Total_Compras;

-- Ver productos disponibles
SELECT 'PRODUCTOS DISPONIBLES' as Reporte;
SELECT Id_Producto, Nombre, Cantidad, Valor_Unitario 
FROM Producto 
ORDER BY Id_Producto;

-- Ver clientes
SELECT 'CLIENTES REGISTRADOS' as Reporte;
SELECT Id_Cliente, Nombre, Fecha_Nacimiento 
FROM Cliente 
ORDER BY Id_Cliente;

-- Ver ventas recientes
SELECT 'VENTAS REALIZADAS' as Reporte;
SELECT v.Id_Venta, v.Descripcion, v.Valor_Total, 
       COUNT(dv.Id_Producto) as Productos,
       SUM(dv.Cantidad_Producto) as Total_Items
FROM Venta v
LEFT JOIN Detalle_Venta dv ON v.Id_Venta = dv.Id_Venta
GROUP BY v.Id_Venta
ORDER BY v.Id_Venta;

-- Productos más vendidos
SELECT 'PRODUCTOS MÁS VENDIDOS' as Ranking;
SELECT 
    p.Nombre as Producto,
    SUM(dv.Cantidad_Producto) as Total_Vendido,
    SUM(dv.Cantidad_Producto * p.Valor_Unitario) as Valor_Total_Ventas
FROM Detalle_Venta dv
JOIN Producto p ON dv.Id_Producto = p.Id_Producto
GROUP BY p.Id_Producto
ORDER BY Total_Vendido DESC;

-- Clientes con más compras
SELECT 'CLIENTES CON MÁS COMPRAS' as Ranking;
SELECT 
    c.Nombre as Cliente,
    COUNT(DISTINCT dv.Id_Venta) as Compras_Realizadas,
    SUM(dv.Cantidad_Producto) as Productos_Comprados
FROM Cliente c
JOIN Compra comp ON c.Id_Cliente = comp.Id_Cliente
JOIN Detalle_Venta dv ON comp.Id_Producto = dv.Id_Producto
GROUP BY c.Id_Cliente
ORDER BY Compras_Realizadas DESC;

-- Ventas por línea de producto
SELECT 'VENTAS POR LÍNEA DE PRODUCTO' as Reporte;
SELECT 
    lp.Nombre as Linea_Producto,
    COUNT(DISTINCT dv.Id_Venta) as Ventas,
    SUM(dv.Cantidad_Producto) as Unidades_Vendidas,
    SUM(dv.Cantidad_Producto * p.Valor_Unitario) as Valor_Total
FROM Linea_Producto lp
JOIN Producto p ON lp.Id_Linea = p.Id_Linea
JOIN Detalle_Venta dv ON p.Id_Producto = dv.Id_Producto
GROUP BY lp.Id_Linea
ORDER BY Valor_Total DESC;
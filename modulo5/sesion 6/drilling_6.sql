GRANT ALL PRIVILEGES ON DATABASE evaluacion_6 TO postgres;
CREATE TABLE empresa(
	rut VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(120),
	direccion VARCHAR(120),
	telefono VARCHAR(15),
	correo VARCHAR(80),
	web VARCHAR(50)
);

CREATE TABLE herramienta(
	id_herramienta INT PRIMARY KEY,
	nombre VARCHAR(120),
	precio_dia MONEY
);

CREATE TABLE cliente(
	rut VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(120),
	correo VARCHAR(80),
	direccion VARCHAR(120),
	celular VARCHAR(15)
);

CREATE TABLE arriendo(
	folio INT PRIMARY KEY,
	fecha DATE,
	dias INT,
	valor_dia INT,
	garantia VARCHAR(30),
	id_herramienta INT,
	rut_cliente VARCHAR(10)
);

ALTER TABLE arriendo 
ADD CONSTRAINT fk_id_herramienta 
FOREIGN KEY(id_herramienta) 
REFERENCES herramienta(id_herramienta);

ALTER TABLE arriendo 
ADD CONSTRAINT fk_rut_cliente 
FOREIGN KEY(rut_cliente) 
REFERENCES cliente(rut);

COMMIT;

	--iniciando una transacción
BEGIN;

--asegurando el primer estado creando un punto de estado
--SAVEPOINT nombre_save_point;
SAVEPOINT primero;
begin;
--Inserte 5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);

SAVEPOINT segundo;

--Inserte 3 clientes.
INSERT INTO cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);							  
							  



--si estoy contento y sucede todo bien, realizamos un commit
COMMIT;



--iniciando una transacción
BEGIN;

--asegurando el primer estado creando un punto de estado
--SAVEPOINT nombre_save_point;
SAVEPOINT primero;

--Inserte 5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);

SAVEPOINT segundo;

--Inserte 3 clientes.
INSERT INTO cliente VALUES('2277722-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('3344433-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('4433344-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);							  

SAVEPOINT tercero;
--Elimina el último cliente
DELETE FROM cliente WHERE rut = '44444444-4';

SAVEPOINT cuarto;
--Elimina la primera herramienta.
DELETE FROM herramienta WHERE id_herramienta = 1;

SAVEPOINT quinto;
--Inserte 2 arriendos para cada cliente
INSERT INTO arriendo VALUES
	(1,'2020/01/15',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
   	(2,'2022/11/10',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
   	(3,'2010/01/15',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
   	(4,'2022/11/10',3,40000,'Eficacia en solo 3 dias',5,'33333333-3');
INSERT INTO empresa VALUES('11111111-1','Arrienda Herramientas','0123 Avenida Real',1234567890,'datosarriendo@herramientas.es','arrimientas.es');
	
--1. Listar todos los arriendos con las siguientes columnas: 
--Folio, Fecha, Días, ValorDia, NombreCliente, RutCliente.  
SELECT a.folio, a.fecha, a.dias, a.valor_dia, c.nombre, c.rut FROM arriendo AS a
JOIN cliente AS c
ON a.rut_cliente=c.rut;
-- Listar los clientes sin arriendos.
SELECT c.nombre FROM cliente AS c
LEFT JOIN arriendo AS a
ON c.rut = a.rut_cliente
WHERE a.rut_cliente is NULL;
--Liste RUT y Nombre de las tablas empresa y cliente. 
SELECT rut, nombre FROM empresa
UNION
SELECT rut, nombre FROM cliente;

SELECT c.rut, c.nombre, e.rut, e.nombre FROM empresa as c
CROSS JOIN cliente as e;

--Liste la cantidad de arriendos por mes. 
SELECT COUNT(EXTRACT (MONTH FROM fecha)) AS cantidad_arriendos, 
EXTRACT(MONTH FROM fecha) AS mes_arriendo, 
EXTRACT(YEAR FROM fecha) AS año
FROM arriendo
GROUP BY mes_arriendo, año;

SELECT*FROM arriendo;
			  
SELECT EXTRACT(YEAR FROM fecha) AS año,
EXTRACT(MONTH FROM fecha) AS mes,
COUNT(folio) AS cantidad_arriendos 
FROM arriendo 
GROUP BY año,mes;			  
			  
select*from arriendo;
select*from cliente;



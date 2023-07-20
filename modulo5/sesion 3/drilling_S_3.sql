CREATE TABLE empresa(
	rut VARCHAR (12) PRIMARY KEY,
	nombre VARCHAR(120),
	direccion VARCHAR(120),
	telefono VARCHAR (15),
	correo VARCHAR(80),
	web VARCHAR(50)
);
CREATE TABLE cliente(
	rut_cliente VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR(120),
	direccion VARCHAR(120),
	correo VARCHAR(80),
	celular VARCHAR(15)
);
CREATE TABLE herramientas(
	herramienta_id INT PRIMARY KEY,
	nombre VARCHAR(120),
	precio_dia MONEY
);

CREATE TABLE arriendo(
	folio INT PRIMARY KEY,
	fecha DATE,
	dias INT,
	valor_dia INT,
	garantia VARCHAR(30),
	herramienta_id INT,
	rut_cliente VARCHAR(10)
);

ALTER TABLE arriendo ADD CONSTRAINT fk_herramienta_id
FOREIGN KEY(herramienta_id)REFERENCES herramientas(herramienta_id);

ALTER TABLE arriendo ADD CONSTRAINT fk_rut_cliente
FOREIGN KEY(rut_cliente)REFERENCES cliente(rut_cliente);

INSERT INTO empresa VALUES ('1111111-1', 'Arriendo Herramientas', 'Los Aromos, 19', '4589302', 'ah@ah.cl', 'www.ah.cl');
INSERT INTO herramientas VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);
INSERT into cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);
INSERT into arriendo VALUES(1,'12/11/22',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
                           (2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
                           (3,'12/11/22',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
                           (4,'12/11/22',3,40000,'Eficacia en solo 3 dias',4,'33333333-3');


--PROBANDO--
SELECT * FROM arriendo;
SELECT * FROM cliente;
-- liste clientes cuyo nombre contenga la a
SELECT nombre FROM cliente WHERE nombre LIKE '%a%';
--liste los arriendos del cliente con rut 33333333-3
SELECT * FROM arriendo WHERE rut_cliente = '33333333-3';
SELECT folio FROM arriendo WHERE rut_cliente = '33333333-3';
--liste todas las herramientas
select nombre FROM herramientas;
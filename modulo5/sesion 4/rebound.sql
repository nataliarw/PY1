CREATE TABLE empresa(
	rut_empresa VARCHAR(12) PRIMARY KEY,
	nombre VARCHAR(50),
	direccion VARCHAR (255),
	telefono VARCHAR (11),
	correo VARCHAR (255),
	web VARCHAR (40)
);
CREATE TABLE cliente(
	rut_cliente VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(30),
	correo VARCHAR(255),
	direccion VARCHAR(255),
	celular VARCHAR(11),
	alta BOOLEAN
);
CREATE TABLE tipo_vehiculo(
	tipo_vehiculo_id INT PRIMARY KEY,
	nombre VARCHAR(255)
);

CREATE TABLE marca(
	marca_id INT PRIMARY KEY,
	marca VARCHAR(255)
);

CREATE TABLE vehiculo(
	vehiculo_id INT PRIMARY KEY,
	patente VARCHAR(6),
	modelo VARCHAR(255),
	color VARCHAR (255),
	precio INT,
	frecuencia_mantencion INT,
	marca_id INT,
	tipo_vehiculo_id INT
);

CREATE TABLE venta(
	folio INT PRIMARY KEY,
	fecha DATE,
	monto INT,
	vehiculo_id INT,
	rut_cliente VARCHAR(10)	
);

CREATE TABLE mantencion(
	mantencion_id INT PRIMARY KEY,
	fecha DATE,
	trabajos_realizados VARCHAR(255),
	folio INT
);
ALTER TABLE vehiculo DROP COLUMN marca;

ALTER TABLE mantencion ADD CONSTRAINT fk_folio
FOREIGN KEY(folio) REFERENCES venta(folio);

ALTER TABLE vehiculo ADD CONSTRAINT fk_marca_id
FOREIGN KEY(marca_id)REFERENCES marca(marca_id);



ALTER TABLE vehiculo ADD CONSTRAINT fk_tipo_vehiculo_id
FOREIGN KEY(tipo_vehiculo_id) REFERENCES tipo_vehiculo(tipo_vehiculo_id);

ALTER TABLE venta ADD CONSTRAINT fk_rut_cliente
FOREIGN KEY(rut_cliente) REFERENCES cliente(rut_cliente);

ALTER TABLE venta add CONSTRAINT fk_vehiculo_id
FOREIGN KEY(vehiculo_id) REFERENCES vehiculo(vehiculo_id);


--• Inserte los datos de una empresa. --
INSERT INTO empresa VALUES ('20555333-2', 'AUTOPART', 'Los conejos 456', '5689473', 'autopart@autopart.cl', 'www.autopart.cl');

--• Inserte 2 tipos de vehículo. 
INSERT INTO tipo_vehiculo VALUES (567, 'camioneta');
INSERT INTO tipo_vehiculo VALUES (897, 'SUV');
--• Inserte 3 clientes. 
INSERT INTO cliente VALUES ('20555333-2', 'Juan Gonzalez','juan@gmail.com', 'Santiago', '569984738', true);
INSERT INTO cliente VALUES ('1111111-1', 'Juana Perez','juana@gmail.com', 'Santiago', '33493829',true);
INSERT INTO cliente VALUES ('22222222-2', 'Maria Nuñez','maria@gmail.com', 'Valparaiso', '4444444',false);
--• Inserte 2 marcas. 
INSERT INTO marca VALUES (999, 'Subaru');
INSERT INTO marca VALUES (777, 'Audi');
--• Inserte 5 vehículos. vehiculo_id INT PRIMARY KEY,
INSERT INTO vehiculo VALUES(1,'RD3456', 'RRRR', 'azul', 3000000, 2, 999, 567);
INSERT INTO vehiculo VALUES(2, 'gf3456', 'ttt', 'blanco', 4000000, 4, 777, 567);
INSERT INTO vehiculo VALUES(3, 'gh3456', 'yyyy', 'gris', 5600000, 1, 777, 897);
INSERT INTO vehiculo VALUES(4, 'we3456', 'uuuu', 'morado', 500000, 4, 999, 897);
INSERT INTO vehiculo VALUES(5, 'pt3456', 'jjjj', 'azul', 9000000, 2, 777, 897);

SELECT  * FROM cliente;
--• Elimina el último cliente. 
DELETE FROM cliente WHERE rut_cliente='22222222-2';
--• Inserte 1 venta para cada cliente. 
INSERT INTO venta VALUES(1,'2023-08-3', 300000, 1, '20555333-2');
INSERT INTO venta VALUES(2,'2023-06-20', 2500000, 4, '1111111-1');

--• Modifique el nombre del segundo cliente. 
UPDATE cliente SET nombre = 'Pedro Perez' WHERE rut_cliente='1111111-1';
--• Liste todas las ventas.
SELECT * FROM venta;
--• Liste las ventas del primer cliente. 
SELECT * FROM venta WHERE folio = 1; 
--• Obtenga la patente de todos los vehículos.
select patente FROM vehiculo;
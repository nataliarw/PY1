CREATE TABLE clientes(
	cliente_id SERIAL PRIMARY KEY,
	nombre_cliente VARCHAR(50),
	ciudad VARCHAR(50)
);
CREATE TABLE articulos(
	codigo INT PRIMARY KEY, 
	nombre_articulo VARCHAR(50),
	precio DECIMAL (10,2)
);

CREATE TABLE detalle_ordenes(
	detalle_orden_id INT,
	fecha DATE,
	cantidad INT,
	codigo INT,
	cliente_id INT,
	CONSTRAINT fk_cliente_id FOREIGN KEY(cliente_id) 
	REFERENCES clientes(cliente_id),
	CONSTRAINT fk_codigo FOREIGN KEY(codigo) 
	REFERENCES articulos(codigo)
);

INSERT INTO clientes (nombre_cliente, ciudad) VALUES
('Martín', 'Santiago'),
('Herman','Valparaíso'),
('Pedro', 'Concepción');

select * from clientes;

INSERT INTO articulos (codigo, nombre_articulo, precio) VALUES
('3786', 'Red', 35.00),
('4011', 'Raqueta', 65.00),
('9132', 'Paq3', 4.75),
('5794', 'Paq6', 5.00),
('3141', 'Funda', 10.00);
 select * from articulos
 
 INSERT INTO detalle_ordenes (detalle_orden_id, fecha, cantidad, codigo, cliente_id) VALUES
 (2301, '2020-02-23', 3, '3786', 1),
 (2301, '2020-02-23', 6, '4011', 1),
 (2301, '2020-02-23', 8, '9132', 1),
 (2302, '2020-02-25', 4, '5794', 2),
 (2303, '2020-02-27', 2, '4011', 3),
 (2303, '2020-02-27', 2, '3141', 3); 
 select * from detalle_ordenes;
 
select nombre_cliente from clientes;
select nombre_cliente, ciudad from clientes;
select * from clientes where ciudad = 'Santiago';
select count (*) from clientes; 
select count (*) as total_clientes from clientes;
select * from clientes order by nombre_cliente;
select * from clientes order by nombre_cliente desc;
select * from clientes order by nombre_cliente asc;
select count(*) from clientes where ciudad = 'Santiago'; --para todos los clientes de una ciudad
select * from clientes where nombre_cliente like 'P%';
select * from clientes where nombre_cliente like '%o';
select * from clientes where nombre_cliente like '%o%'; -- todo lo que tenga o
select * from clientes where nombre_cliente like upper ('p%');
select * from clientes where lower (nombre_cliente) like 'p%';

select * from clientes where ciudad ='Valparaíso' and nombre_cliente = 'Herman';
select * from clientes where ciudad ='Valparaíso' and nombre_cliente like '%Herman%';
-- between--
select * from detalle_ordenes where fecha between '2020-02-23' and '2020-02-25';
select * from detalle_ordenes where cantidad >=6;
--sum--

select sum (cantidad) as cantidad_total from detalle_ordenes;
--avg--
select avg(cantidad) as average from detalle_ordenes;

--max--
select max (fecha) from detalle_ordenes;
--min --
select min (fecha) from detalle_ordenes;






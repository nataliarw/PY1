--Crear tabla “editoriales”, con los atributos código y nombre. 
--Definir el código como llave primaria. 2. Crear tabla “libros”, 
--con los atributos código, título, y codigoeditorial. Definir el código como
--llave primaria, y codigoeditorial como llave foránea, 
--referenciando a la tabla editoriales.
BEGIN;
CREATE TABLE editoriales(
	codigo SERIAL PRIMARY KEY,
	nombre VARCHAR (50)
);

CREATE TABLE libros(
	codigo SERIAL PRIMARY KEY,
	titulo VARCHAR (100),
	codigo_editorial INT
);
ALTER TABLE libros ADD CONSTRAINT fk_codigo_editorial 
FOREIGN KEY (codigo_editorial) REFERENCES editoriales(codigo);

SAVEPOINT primero;
INSERT INTO editoriales(nombre) VALUES 
	('Anaya'),
	('Andina'),
	('S.M');
	
INSERT INTO libros(titulo, codigo_editorial) VALUES 
	('Don Quijote de la Mancha I', 1),
	('El Principito', 2),
	('El Principe', 3), 
	('Diplomacia', 3),
	('El Quijote de la Mancha II', 1);
SAVEPOINT segundo;
ALTER TABLE libros ADD autor VARCHAR(50), ADD precio MONEY;
SAVEPOINT tercero;

UPDATE libros SET autor =CASE 
	WHEN codigo = 1 THEN 'Miguel de Cervantes'
	WHEN codigo = 2 THEN 'Antoine Saint Exupery'
	WHEN codigo = 3 THEN 'Maquiavelo'
	WHEN codigo = 4 THEN 'Henry Kissinger'
	WHEN codido = 5 THEN 'Miguel de Cervantes'
	END
WHERE codigo IN (1,2,3,4,5);


UPDATE libros SET precio =CASE 
	WHEN codigo = 1 THEN 150
	WHEN codigo = 2 THEN 120
	WHEN codigo = 3 THEN 180
	WHEN codigo = 4 THEN 170
	WHEN codido = 5 THEN 140
	END
WHERE codigo IN (1,2,3,4,5);
SAVEPOINT seis;
INSERT INTO libros (titulo, codigo_editorial, autor, precio) VALUES
('monos feos', 1, 'Francisco Puelma', 120),
('Bluey', 2, 'Pepa Pig', 150);
SAVEPOINT siete;
ROLLBACK;
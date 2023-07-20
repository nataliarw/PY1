GRANT ALL PRIVILEGES ON DATABASE dvdrental TO postgres;
--se hizo restore para cargar el archivo solicitado 

SELECT * FROM category;

SELECT * FROM inventory;

SELECT * FROM customer;

SELECT * FROM film_category;

SELECT * FROM rental;

SELECT * FROM film;

SELECT * FROM payment;

SELECT * FROM address;

SELECT * FROM language;
SELECT * FROM staff;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM store;
SELECT * FROM actor;
SELECT * FROM film_actor;


--4. Construye las siguientes consultas: 
--• Aquellas usadas para insertar, modificar y eliminar un Customer, Staff y Actor. 
--INSERTS
INSERT INTO customer VALUES(600, 2, 'Juan', 'Perez', 'juan.perez@gmail.com', 610, true);							
INSERT INTO staff VALUES(3,'Juan', 'Perez', 5, 'juan.perez@gmail.com', 1, true, 'Juan', 'xxxxx', '2006-05-16 xxx', link);
INSERT INTO actor VALUES(201, 'Juan', 'Perez', 'xxxxx');
--UPDATES
UPDATE customer
SET first_name = 'Juana' 
WHERE customer_id = 600;

UPDATE staff
SET first_name = 'Juana' 
WHERE staff_id = 3;

UPDATE actor
SET first_name = 'Juana' 
WHERE actor_id = 201;
--DELETES
DELETE FROM customer 
WHERE customer_id = 600;

DELETE FROM staff 
WHERE staff_id = 3;

DELETE FROM actor 
WHERE actor_id = 201;

--• Listar todas las “rental” con los datos del “customer” dado un año y mes. 
SELECT r.* FROM rental as r
JOIN customer as c
ON r.customer_id = c.customer_id
WHERE r.rental_date BETWEEN '2005-06-01' AND '2005-06-30'

SELECT r.* FROM rental as r
JOIN customer as c
ON r.customer_id = c.customer_id
WHERE EXTRACT (YEAR FROM r.rental_date) = '2005'
AND
EXTRACT(MONTH FROM r.rental_date) ='06';


--• Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”. 
SELECT payment_id as numero, payment_date as fecha, amount as total FROM payment
ORDER BY fecha DESC;

SELECT payment_id as numero, CAST (payment_date as date) fecha, amount as total FROM payment
ORDER BY fecha DESC;

--• Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0
SELECT * FROM film 
WHERE rental_rate > 4 and release_year = '2006'
ORDER BY title;

--5. Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, 
--   si éstas pueden ser nulas, y su tipo de dato correspondiente.
SELECT
    t1.TABLE_NAME AS tabla_nombre,
    t1.COLUMN_NAME AS columna_nombre,
    t1.COLUMN_DEFAULT AS columna_defecto,
    t1.IS_NULLABLE AS columna_nulo,
    t1.DATA_TYPE AS columna_tipo_dato,
    COALESCE(t1.NUMERIC_PRECISION,
    t1.CHARACTER_MAXIMUM_LENGTH) AS columna_longitud,
    PG_CATALOG.COL_DESCRIPTION(t2.OID,
    t1.DTD_IDENTIFIER::int) AS columna_descripcion,
    t1.DOMAIN_NAME AS columna_dominio
FROM 
    INFORMATION_SCHEMA.COLUMNS t1
    INNER JOIN PG_CLASS t2 ON (t2.RELNAME = t1.TABLE_NAME)
WHERE 
    t1.TABLE_SCHEMA = 'public'
ORDER BY
    t1.TABLE_NAME;

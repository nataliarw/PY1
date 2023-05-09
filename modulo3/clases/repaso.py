# """ Se solicita crear un diccionario en Python para almacenar los precios
# de diferentes productos en una tienda en línea.
# Las claves del diccionario serán los nombres de los productos y los valores serán los precios de los productos.
# A continuación, se solicita recorrer el diccionario e imprimir los productos cuyos precios son superiores a 50 dólares. Finalmente, se debe calcular el precio total de los productos cuyos nombres empiezan con la letra 'C' y mostrarlo en pantalla.

precios = {'camisa': 30,'pantalon': 50,'zapatos': 80,'calcetines': 10,'chaqueta': 100 } 
precio_total = 0
contador_c=0
for producto, precio in precios.items():
    if precio > 50:
        print (producto)
    
    if producto[0]=="c":
        precio_total +=precio
        contador_c +=1
print(precio_total, "y el promedio es", precio_total/contador_c)
# coleccion de elementos que van almacenados por clave y valor
# declaracion de diccionarios con llaves o con dict()

estudiantes ={
    "maria" :30,
    "juanita" : 22,
    "jose" : 40,
    "marta" : 35
}

print(estudiantes)
# para acceder al valor de una clave
print(estudiantes["maria"])

# remover clve de diccionario
del estudiantes["maria"]
print(estudiantes)

claves = estudiantes.keys()
print(claves)

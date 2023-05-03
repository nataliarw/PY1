"""
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos números, 
y otra que divida dos números. Adicionalmente, crear una función que acepte dos números como parámetros 
y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división. Los resultados se deben 
almacenar en un diccionario, cuyas claves serán: Suma, Resta, Multiplicación y División, y los valores de cada clave 
serán los resultados obtenidos con la función creada anteriormente. 
"""
numeros = input('ingrese 2 numeros distintos separados por coma (,) :')
numeros = [ int(i) for i in numeros.split(',') ]
diccionario ={}
# funciones matematicas basicas
def sumar():
    suma=sum(numeros)
    return suma
def restar():
    resta = numeros[0] -numeros[1]
    return resta
def multi():
    multipli= numeros[0] *numeros[1]
    return multipli
def dividir():
    divi= numeros[0]//numeros[1]
    return divi
# asegurando que sean dos parametros y recibiendo resultados como tupla
def check_length_two(num):
    if len(num) == 2:
        tupla=(sumar(), restar(), multi(), dividir()) 
        return tupla
    else:
        numeros = input('Debe ingresar 2 numeros separados por coma (,) :')
        numeros = [ int(i) for i in numeros.split(',') ]
# almacenando los resultados en un diccionario (el mismo resultado se pudo hacer dentro de la otra
# funcion pero queria llenar de datos la variable global y si lo hacia en la misma 
# funcion check_lenght, la funcion me daba dos resultados, la tupla y el diccionario)
def construyendo(num):
    claves= check_length_two(num)
    keys=["Suma", "Resta", "multiplicacion", "division"]
    dic1 = zip(keys, claves)

    return dict(dic1)
    
    
check_length_two (numeros) 
# agregando los datos del diccionario a la variable global diccionario
diccionario = construyendo(numeros)
print(diccionario)
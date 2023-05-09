def suma(*numeros): 
    # el * hace los parametros de la funcion iterables entonces puedo pasarle los argumentos que yo quiera 
    resultado = 0 
    for numero in numeros: 
        resultado += numero 
        print(resultado) # ejemplos de suma iterable para la funcion
suma(2, 5) 
suma(3, 4, 5, 6, 7) 
suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
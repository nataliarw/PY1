# Realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b por parte del usuario en consola

# import math
# cateto_a = float(input("ingrese valor de un cateto del triangulo: "))
# cateto_b = float(input("ingrese valor del otro cateto del triangulo: "))

# hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
# print(f"la hipotenusa es {hipotenusa}")


# from telnetlib import theNULL


# palabraUno = (input("ingrese una frase: "))
# palabraDos = (input("ingrese otra frase: "))

# if palabraUno == palabraDos or len(palabraUno) == len(palabraDos): 
#     print("su texto es igual o tiene el mismo tamaño") 
# else: 
#     print("no tienen el mismo tamaño o no son iguales")
# import time
# n=5
# while n>= 1:
#     print(n)
#     n -=1
#     time.sleep(1)
# print("BOOM")

# for i in range(5,0,-1):

#     print(i)

# print("Booom")

'''Aquí te explico los argumentos de la función range(start, stop, step):
start: el valor inicial de la secuencia. En este caso, es 5.
stop: el valor final de la secuencia. En este caso, es 0. Pero como el límite superior no se incluye, la secuencia termina antes de llegar a 0.
step: la cantidad en la que se incrementa o decrementa la secuencia. En este caso, es -1, lo que indica que la secuencia se genera en decremento de 1 en 1.'''

# Realizar la ejecución de un menú utilizando el lenguaje Python, 
# donde se le indiquen varias opciones a seleccionar por el usuario y 
# una opción para salir del menú.
# Utilizar ciclos y estructuras condicionales.
# opcion = ""
# while opcion != "4":
#     print ("hola, bienvenido")
#     print("1.opcion 1")
#     print("2..opcion 2")
#     print("3..opcion 3")
#     print("4..salir de menu")
#     print("elija una opcion: ")
    
#     opcion =input()
#     if opcion == "1":
#         print("ha elegido opcion 1")
#     elif opcion == "2":
#         print ("ha elegido opcion 2")
#     elif opcion =="3":
#         print("ha elegido opcion 3")
#     elif opcion =="4":
#         print("gracias por su visita")
#     else:
#          print("elija una opcion valida")


while True: 
    opcion = int(input("Hola, bienvenido\n " 
                       "1.- Saludar\n " "2.- preguntar que hay en la tele\n " 
                       "3.- que opinas de la música que escucho?\n" 
                       "4.- que estás sintiendo ahora?\n" 
                       "5.- Salir\n\n" "Ingresa una opción => ")) 
    match opcion: 
        case 1: 
            print("Hola, que tal?") 
        case 2: 
            print("No hay nada bueno") 
        case 3: 
            print("Es buena música") 
        case 4: 
            print("Tengo hambre!") 
        case 5: 
            print("Nos vemos!") 
            break 
        case _: print("Esa opcion no es válida!")
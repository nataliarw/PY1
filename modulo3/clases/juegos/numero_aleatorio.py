'''
imula un juego de adivinanza,

donde el jugador debe adivinar un número aleatorio generado por el programa.

El programa le dará pistas al jugador sobre si el número ingresado es mayor o menor que el número generado,

y seguirá pidiendo al jugador que ingrese un número hasta que adivine correctamente.
'''

import random
numero_random = random.randint(1,100)
# print(numero_random)
print("""Bienvenido al juego de adivinanza, 
      adivine un numero entre 1 y 100, tiene
      cuatro intentos""")

adivinanza = 3
contador = 0
while adivinanza != numero_random and contador <= 4 :
    adivinanza =int(input("ingrese un numero del 1 al 100:"))
    contador +=1
    if adivinanza>numero_random:
        print("el numero a adivinar es menor que el elegido")
    elif adivinanza<numero_random:
        print("el numero a adivinar es mayor que el ingresado")
    else:
        print(f"adivinaste! el numero era {numero_random} y lo adivinaste en {contador} intentos")
print("Te quedaste sin intentos, lo siento")
# Escribir un programa que analice un número, e indique si es positivo o negativo,
# y si es par o impar. En caso de ser cero, también indicarlo. Se debe usar la expresión
# if -elif -else, y no usar subcondiciones
# en su lugar, usar condiciones anidadas. REBOUND M3 S6


numero = int(input("Escriba un numero: "))

if numero == 0:
    print("el numero ingresado es cero")

elif numero > 0:
    if numero % 2 == 0: 
        print (f"El número {numero} es positivo y par.")
    else:
        print(f"el numero {numero} es positivo e impar")
elif numero < 0:
    if numero % 2 ==0:
        print(f"El número {numero} es negativo y par.")
    else:  
        print(f"el numero {numero} es negativo e impar")

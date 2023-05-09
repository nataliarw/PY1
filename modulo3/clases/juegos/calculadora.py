'''
Se pide realizar una calculadora declarando funciones para cada tipo de calculo que se realice

realizar un menu con opciones para seleccionar que calculo se desea realizar

el ingreso es por consola, requerir al usuario la opcion y numeros al que se realizara el calculo

verificar errores de ingreso

verificar division por cero
'''


def suma(num1,num2):
  return( num1 + num2)
   


def resta(num1: float, num2: float):
    restar = num1 - num2
    return restar


def multiplica(num1, num2) -> float:
    multiplicar = num1 * num2
    return multiplicar


def divide(num1, num2):
    if num2 == 0:
        return None
    else:
        dividir = num1/num2
        return dividir


def opciones():
    print("""Bienvenidos a la Calculadora
                1. sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                5. Salir""")





def calculadora():
    while True:
        try:
            opciones()
            opcion = (input("ingrese la opcion 1, 2, 3, 4 o 5: "))
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            match opcion:
                case '1':
                    print(f"el resultado de la {opcion} es {suma(num1, num2)}")

                case '2':
                    print(f"el resultado de la {opcion} es {resta(num1, num2)}")
                case '3':
                    print(f"el resultado de la {opcion} es {multiplica(num1,num2)}")
                case '4':
                    divide(num1, num2)
                    if divide(num1, num2) is not None:
                        print(f"el resultado de la {opcion} es {divide(num1,num2)}")
                    else:
                        print("Usted intento dividir por cero, lo que es imposible")
                    
                case '5':
                    print("Gracias por usar esta calculadora")
                    break
                case  _:
                    print("Elija una opcion valida")
        except Exception as e:
            print("Error", e)

calculadora()

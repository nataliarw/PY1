# Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el orden de mayor a menor.

#  test #1
# numerouno = input("escriba el 1er numero: ")


# numerodos = input("escriba el 2do numero: ")

# while numerouno == numerodos:
#     numerodos = input("escriba un 2do numero distinto del 1er: ")



# numerotres = input("escriba el 3er numero: ")

# while numerotres in [numerodos, numerouno]:
#     numerotres = input("escriba un 3er numero distinto del 1er y el 2do: ")


# print('numeros validos')
# numerouno = int(numerouno)
# numerodos = int(numerodos)
# numerotres = int(numerotres)

# a = max(numerouno, numerodos, numerotres)
# b = min(numerouno, numerodos, numerotres)
# c = (numerouno + numerodos + numerotres) - a - b
# print(f"los numeros en orden descendente son {a}, {c} y {b}")



## otra forma

numeros = input('ingrese 3 numeros distintos separados por coma (,) :')
numeros = [ int(i) for i in numeros.split(',') ]

def check_length_three(num: list) -> bool:
    if len(num) == 3:
        return True
    else:
        return False

def check_no_distintos(num: list) -> bool:
    if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
        return True
    else:
        return False

def sort_no(num: list) -> list:
    print(num)
    return sorted(num, reverse=True)


while check_length_three(numeros) == False or check_no_distintos(numeros) == False:
    numeros = input('Debe ingresar 3 numeros distintos separados por coma (,) :')
    numeros = [ int(i) for i in numeros.split(',') ]
    
# print('numeros seleccionados:', numeros)
numeros= sort_no(numeros)
print("Los numeros ingresados ordenados de mayor a menor son:")
print(*numeros, sep=", ")

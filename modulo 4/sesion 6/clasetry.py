def division_ingreso():
    try:
        n1=int(input("Ingreso un numero: "))
        n2= int(input("ingrese segundo numero: "))
        resultado= n1/n2
        print(resultado)
    except Exception as e:
        print(f"error: {e} no permitido")
        division_ingreso()
        
# division_ingreso()

class CostumeException(Exception):
    pass
def excepcion_propia():
    try:
        ingreso= int(input("Ingrese edad: "))
        if ingreso<0:
            raise CostumeException("Excepcion propia ejecutada")
        print("edad: ", ingreso)
    except ValueError:
        print("error ingreso no valido")
        


def excepcion_propia_caso():
    try:
        ingreso= int(input("Ingrese edad: "))
        if ingreso<0:
            raise CostumeException("Excepcion propia ejecutada")
        print("edad: ", ingreso)
    except ValueError:
        print("error ingreso no valido")
    except CostumeException as e:
        print(f"error: {e} y manejada")
        
excepcion_propia_caso()
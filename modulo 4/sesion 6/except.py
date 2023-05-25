class CostumeException(Exception):
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje)
        self.codigo=codigo
        
def excepcion_propia():
    try:
        edad= int(input("Ingrese edad: "))
        if edad<0:
            raise CostumeException("Excepcion propia ejecutada", 460)
        print("edad: ", edad)
    except ValueError:
         print("error ingreso no valido")
    except CostumeException as e:
            print(f"error: {e} y manejada")
            print(f"Error:{e.codigo}") 
excepcion_propia() 
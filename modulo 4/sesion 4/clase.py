from multipledispatch import dispatch

class Animal:
    # def __init__(self, nombre:str, raza:str, edad:int, peso:float):
    #     self.nombre=nombre
    #     self.raza=raza
    #     self.edad=edad
    #     self.peso=peso
        
    @dispatch(str, str,int,float)
    def __init__(self, nombre, raza, edad, peso):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso   
caballo = Animal("Zeus", "Pura Sangre", 5, 450.3)
leon = Animal("Boulder", "Atlas", 10, 130.1)

print(caballo.peso)

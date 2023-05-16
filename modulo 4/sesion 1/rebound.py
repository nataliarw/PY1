'''
REBOUND DISEÑAR CLASE
'''
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso
        
    def comer(self):
        print(f"el animal {self.nombre} está comiendo")
    def caminar(self):
        print(f"el animal {self.nombre} está caminando")
    def dormir(self):
        print(f"el animal {self.nombre} está durmiendo")
        
perro = Animal("Charlie", "Beagle", 10, 10.5)
gato = Animal("Kitty", "Siames", 5, 8.3)
print("su nombre es", perro.nombre,"y pesa", perro.peso, "kilos")
print(vars(gato))
gato.comer()




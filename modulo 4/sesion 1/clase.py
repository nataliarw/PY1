class animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso
        
    #constructor sin parametros
    def __init__(self, nombre=None, raza=None, edad=None, peso=None):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso

perro = animal("Charlie", "Beagle", 10, 10.5)
gato = animal("Kitty", "Siames", 5, 8.3)
jirafa=animal()
print("su nombre es", perro.nombre,"y pesa", perro.peso, "kilos")
jirafa.nombre = "minie"
jirafa.edad = 28
print(jirafa.nombre)
print(vars(gato))

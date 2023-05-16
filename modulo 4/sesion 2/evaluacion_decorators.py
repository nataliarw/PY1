class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self._nombre=nombre
        self._apellido=apellido
        self._sexo=sexo
        self._edad=edad
        self._estatura=estatura
        self._peso=peso
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre (self, nombre):
        self._nombre =nombre
        
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido= apellido
    @property
    def sexo(self):
        return self._sexo
    @nombre.setter
    def sexo (self, sexo):
        self._sexo =sexo
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad (self, edad):
        self._edad =edad
    @property
    def estatura(self):
        return self._estatura
    @estatura.setter
    def estatura (self, estatura):
        self._estatura =estatura
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso (self, peso):
        self._peso =peso
    
    def __str__(self):
        return f"Persona(nombre = {self._nombre}, apellido = {self._apellido}, sexo = {self._apellido}, edad = {self._edad}, estatura={self._estatura}, peso={self._peso})"
        
persona_1 = Persona("Pedro", "Vivas", "masculino", "20 años", "1.78 mts", "68 kg")
persona_2 = Persona("Juan", "Camargo", "masculino", "18 años", "1.8 mts", "75 kg")
    
print(f"el nombre de persona_1 es {persona_1.nombre}  y el apellido de persona_2 es {persona_2.apellido}")   

persona_1.edad = "21 años"
persona_2.apellido = "Santiago"  
print("imprimimos los cambios de nombre de persona_1 y el apellido de persona_2")
print(persona_1)
print(persona_2)
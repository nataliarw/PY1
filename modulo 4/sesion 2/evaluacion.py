class Persona:
    def __init__(self, nombre:str, apellido:str, sexo:str, edad:str, estatura:str, peso:str):
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.edad=edad
        self.estatura=estatura
        self.peso=peso
    # getters
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.estatura
    
    def get_peso(self):
        return self.peso
    # setters 
    def set_nombre(self,nombre):
        self.nombre = nombre
        
    def set_apellido(self,apellido):
        self.apellido = apellido
        
    def set_sexo(self,sexo):
        self.sexo = sexo
        
    def set_edad(self,edad):
        self.edad = edad
        
    def set_estatura(self,estatura):
        self.estatura = estatura
        
    def set_peso(self,peso):
        self.peso = peso
    
                 
persona_1 = Persona("Pedro", "Vivas", "masculino", "20 años", "1.78 mts", "68 kg")
persona_2 = Persona("Juan", "Camargo", "masculino", "18 años", "1.8 mts", "75 kg")
# se setean los nuevos valores de los atributos
persona_1.set_edad("21 años")
persona_2.set_apellido("Santiago")
#para mostrar por pantalla los cambios seria como get
print(persona_1.get_edad())
print(persona_2.get_apellido())
#y asi para ver todo el objeto
print(vars(persona_1))
print(vars(persona_2))


class Persona:
    def __init__ (self, nombre, apellido, rut):
        self._nombre = nombre #el guion da cuenta de atributo privado
        self._apellido = apellido
        self._rut = rut

    #getter y setters
    @property #este es el get, mas buena onda con python
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def rut(self):
        return self._rut
    @rut.setter
    def rut(self, rut):
        self._rut =rut
        
# obj = Persona("maria", "perez", "3456-5")
# print(obj.nombre)  #llama al property, no al atributo

#creando funcion o metodo de la clase
    def get_tipo(self):
        print(f"soy del tipo{self}")
    #print(type{self})
    
    def __str__(self):
        return f"Persona(nombre= {self._nombre}, apellido= {self._apellido}, rut= {self._rut})"

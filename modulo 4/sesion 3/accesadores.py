class Accesadores:
    def __init__(self):
        self.atributo_publico = "puede ser accedido en toda la estructura"
        self._atributo_protected = "puede ser accedida desde su clase y subclases"
        self.__atributo_privado = "solo puede ser accedido en la clase que esta declarada"
        
    def get_variablePrivada(self):
        return self.__atributo_privado
    def set_variablePrivada(self, __atributo_privado):
        self.__atributo_privado = __atributo_privado
    
objeto = Accesadores()
print(objeto.get_variablePrivada())
objeto.set_variablePrivada("pan con palta")
print(objeto.get_variablePrivada())
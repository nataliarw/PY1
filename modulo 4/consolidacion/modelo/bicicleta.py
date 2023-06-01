from modelo.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self._tipo = tipo
        
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    def __str__(self):
        return f'Vehiculo Bicicleta: Marca: {self._marca}, Modelo: {self._modelo}, numero de ruedas: {self._numero_de_ruedas} ruedas, {self.tipo}'
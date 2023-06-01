from modelo.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_de_ruedas)
        self._velocidad =velocidad
        self._cilindrada =cilindrada
        
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
        
    @property
    def cilindrada(self):
        return self._cilindrada
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada
    

    def __str__(self):
        return f'Marca: {self._marca}, Modelo: {self._modelo}, numero de ruedas: {self._numero_de_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc'
    
from modelo.automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self._carga=carga
        
    @property
    def carga(self):
        return self._carga
    @carga.setter
    def carga(self, carga):
        self._carga=carga
    
    def __str__(self):
        return f'Vehiculo de carga: Marca: {self._marca}, Modelo: {self._modelo}, numero de ruedas: {self._numero_de_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc, {self._carga} kilos de carga'
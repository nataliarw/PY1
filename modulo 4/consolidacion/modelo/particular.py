from modelo.automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self._n_puestos = n_puestos 
        
    @property
    def n_puestos(self):
        return self._n_puestos
    @n_puestos.setter
    def n_puestos(self, n_puestos):
        self._n_puestos = n_puestos
    def __str__(self):
        return f'Vehículo Particular: Marca: {self._marca}, Modelo: {self._modelo}, numero de ruedas: {self._numero_de_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc, {self._n_puestos} puestos'
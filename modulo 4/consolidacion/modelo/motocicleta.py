from modelo.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo, n_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        self._n_radios = n_radios
        self._cuadro = cuadro
        self._motor = motor
        
    @property
    def n_radios(self):
        return self._n_radios
    @n_radios.setter
    def n_radios(self, n_radios):
        self._n_radios = n_radios
        
    @property
    def cuadro(self):
        return self._cuadro
    @cuadro.setter
    def cuadro(self, cuadro):
        self._cuadro =cuadro
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, motor):
        self._motor = motor
    def __str__(self):
        return f'Vehículo Motocicleta: Marca: {self._marca}, Modelo: {self._modelo}, numero de ruedas: {self._numero_de_ruedas} ruedas, {self.tipo}, {self._n_radios} radios, tipo de cuadro: {self._cuadro}, motor: {self._motor}'

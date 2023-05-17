from modelo.persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area):
        super().__init__(nombre, apellido, rut)
        self._area = area
        
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, area):
        self._area=area
        
    def __str__(self):
        return f"(nombre={self._nombre}, apellido={self._apellido}, rut= {self._rut}, area={self._area})"
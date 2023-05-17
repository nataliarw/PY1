class Capacidades:
    def __init__(self, ncertificados, rating):
        self._ncertificados =ncertificados
        self._rating = rating
        
    @property
    def ncertificado(self):
        return self._ncertificados
    @ncertificado.setter
    def ncertificados(self, ncertificados):
        self._ncertificados =ncertificados
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        self._rating=rating
        
    def __str__(self) -> str:
        return f"capacidades(ncertificados={self._ncertificados}, rating ={self._rating})"
        
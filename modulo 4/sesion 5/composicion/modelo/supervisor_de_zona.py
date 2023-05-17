
class SupervisorZona():
    def __init__(self, Supervisor, Capacidades, promedio) -> None:
        self._supervisor=Supervisor
        self._capacidades=Capacidades
        self._promedio=promedio
        
    @property
    def supervidor(self):
        return self._supervisor
    
    @supervidor.setter
    def supervisor(self, supervisor):
        self._supervisor=supervisor
    @property
    def capacidades(self):
        return self._capacidades
    @capacidades.setter
    def capacidades(self, capacidades):
        self.capacidades=capacidades
    
    @property
    def promedio(self):
        return self._promedio
    @promedio.setter
    def promedio(self, promedio):
        self._promedio=promedio   
        

class Persona:
    def __init__(self, nombre, apellido, anno) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno


class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto) -> None:
        self.nombre_depto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto


class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self,nombre, apellido, anno)
        Departamento.__init__(self,nombre_dpto, nombre_corto_dpto)
        self.salario = salario

def conocer_instancia(objeto, clase):
    if isinstance(objeto, clase):
        return"Si"
    else:
        return"No"
    
def instanec_1linea(objeto, clase): #FORMA DE HACERLO EN UNA SOLA LINEA
    resultado= "Si" if isinstance(objeto, clase) else "NO"
    return resultado
    
trabajador = Trabajador("Juan", "Perez", "2005","Ingenieria de Software", "IS", "20000")
print(trabajador.__dict__)
print("Es trabajador instancia de Persona:", conocer_instancia(trabajador, Persona))
print("Es trabajador instancia de Departamento:", conocer_instancia(trabajador, Departamento))
print("Es trabajador instancia de Trabajador:", conocer_instancia(trabajador, Trabajador))
print(getattr(trabajador, "nombre"))

# "si" if (isinstance(trabajador, class))
import csv
class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self._marca=marca
        self._modelo=modelo
        self._numero_de_ruedas=numero_de_ruedas
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca=marca
        
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo=modelo
        
    @property
    def numero_de_ruedas(self):
        return self._numero_de_ruedas
    
    @numero_de_ruedas.setter
    def numero_de_ruedas(self, numero_de_ruedas):
        self._numero_de_ruedas = numero_de_ruedas
    
    def guardar_datos_csv(self, nombre_archivo): 
        try:
            archivo = open(nombre_archivo, "a+", newline="")    
            #datos = [(self.__class__, self.__dict__)]    
            archivo_csv = csv.writer(archivo)    
            archivo_csv.writerow([ self.__str__()])    
            archivo.close()  
        except FileNotFoundError:
            print("Error: file not found", nombre_archivo)
        except Exception as e:
            print("Error:", e)
        


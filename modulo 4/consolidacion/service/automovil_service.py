from modelo.automovil import Automovil

class AutomovilService:
    def crear_automovil(self, contador):
        marca= input ("ingrese marca de automovil: ")
        modelo= input ("ingrese modelo de automovil: ")
        numero_de_ruedas= input("ingrese numero de ruedas de automovil: ")
        velocidad =input("ingrese velocidad del automovil: ")
        cilindrada = input("ingrese cilidrada del automovil: ")
        automovil= Automovil(marca,modelo ,numero_de_ruedas, velocidad, cilindrada)
        print(f"Automovil {contador} creado:", automovil)
        return automovil
    def __str__(self):
        return f'Marca: {self._marca}, Modelo: {self._modelo}, {self._numero_de_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc'

   
from modelo.vehiculo import Vehiculo
from modelo.automovil import Automovil
from service.automovil_service import AutomovilService
from modelo.bicicleta import Bicicleta
from modelo.particular import Particular
from modelo.carga import Carga
from modelo.motocicleta import Motocicleta


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", "2", "Carrera")
motocicleta = Motocicleta("BMW", "F800s","2","Deportiva","2T","Doble Viga", "21")
# print(f"{particular} \n {carga} \n {bicicleta} \n {motocicleta}")
# print("Motocicleta es instancia con relacion a Vehículo: ", isinstance(motocicleta, Vehiculo))
# print("Motocicleta es instancia con relacion a Automovil: ", isinstance(motocicleta, Automovil))
# print("Motocicleta es instancia con relacion a Vehículo de carga: ", isinstance(motocicleta, Carga))
# print("Motocicleta es instancia con relacion a Vehículo particular: ", isinstance(motocicleta, Particular))
# print("Motocicleta es instancia con relacion a Bicicleta: ", isinstance(motocicleta, Bicicleta))
# print("Motocicleta es instancia con relacion a Motocicleta: ", isinstance(motocicleta, Motocicleta))
particular.guardar_datos_csv("vehiculos.csv")
carga.guardar_datos_csv("vehiculos.csv")
bicicleta.guardar_datos_csv("vehiculos.csv")
motocicleta.guardar_datos_csv("vehiculos.csv")

print(particular.leer_datos_cvs("vehiculos.csv"))



ingreso = int(input("Cuántos automoviles desea ingresar: "))

i = 1

automovil_service = AutomovilService()
lista=[]
while i <= ingreso:
    print(f"ingrese el automovil {i}: ")
    automovil =automovil_service.crear_automovil(i)
    #automovil.guardar_datos_csv("vehiculos.csv")
    lista.append(automovil.__str__())
    i+=1

# forma alternativa de impresion
# a=1
# for automovil in  lista:
#     print('DATOS DEL AUTOMOVIL:',a, automovil)
#     a+=1

for i in range(len(lista)):
    print("Datos del automovil", i+1,":", lista[i])
    
from modelo.supervisor import Supervisor
class SupervisorService:
    def crear_supervisor(self):
        nombre= input("ingrese nombre del supervisor: ")
        apellido= input ("ingrese apellido de supervisor: ")
        rut = input ("ingrese rut de supervisor: ")
        area =input("ingrese area de supervisor: ")
        #CREAR SUPERVISOR
        supervisor= Supervisor(nombre, apellido, rut, area)
        print("Supervisor Creado", supervisor)
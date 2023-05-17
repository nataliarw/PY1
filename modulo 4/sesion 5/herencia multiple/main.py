from modelo.persona import Persona
from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisor_de_zona import SupervisorZona
# persona=Persona("Juanita", "Gonzalez", "1234-5")
# print(persona)
# print(str(persona))
# persona.get_tipo()

# cliente=Cliente("Juanita","Gonzalez", "1234-5", "10%" )
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()
# def main():
#     #accedemos a la clase a traves de instancias. tb se podria desde el nombre de la clase
#     menu_service= MenuService()
#     cliente_service= ClienteService()
#     supervisor_service = SupervisorService()
    
#     while True:
#         menu_service.imprimir_menu()
#         opcion=input("Ingrese una opcion: ")
#         match opcion:
#             case "1":
#                 cliente_service.crear_cliente()
#             case "2":
#                 supervisor_service.crear_supervisor()
#             case "3":
#                 print("gracias por usar nuestro sistema")
#                 break
#             case _:
#                 print("opcion invalida, intente otra")
    #funcion inicializadora para da un inicio al programa
if __name__ == "__main__":
       # main()
    supervisor_zona =SupervisorZona("maria", "perez","234-5", "agricola", "8", "7", "9")
    print(supervisor_zona.apellido)
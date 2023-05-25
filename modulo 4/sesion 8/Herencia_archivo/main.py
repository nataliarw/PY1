from modelo.persona import Persona
from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService

# persona=Persona("Juanita", "Gonzalez", "1234-5")
# print(persona)
# print(str(persona))
# persona.get_tipo()

# cliente=Cliente("Juanita","Gonzalez", "1234-5", "10%" )
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()
def main():
    #accedemos a la clase a traves de instancias. tb se podria desde el nombre de la clase
    menu_service= MenuService()
    cliente_service= ClienteService()
    supervisor_service = SupervisorService()
    
    while True:
        menu_service.imprimir_menu()
        opcion=input("Ingrese una opcion: ")
        match opcion:
            case "1":
                cliente_service.crear_cliente()
            case "2":
                supervisor_service.crear_supervisor()
            case "3":
                cliente_service.list_clientes()
            case "4":
                rut = input("Ingrese el rut del cliente: ")
                print(cliente_service.get_cliente_by_rut(rut))
                
            case "5":
                print("gracias por usar nuestro sistema")
                break
            case _:
                print("opcion invalida, intente otra")
    #funcion inicializadora para da un inicio al programa
if __name__ == "__main__":
        main()
    #liente_service=ClienteService()
    #print(cliente_service.load_clientes())
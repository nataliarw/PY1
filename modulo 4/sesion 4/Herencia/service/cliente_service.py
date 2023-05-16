from modelo.cliente import Cliente
class ClienteService:
    def crear_cliente(self):
        nombre= input ("ingrese nombre de cliente: ")
        apellido= input ("ingrese apellido de cliente: ")
        rut= input("ingrese rut de cliente: ")
        descuento =input("ingrese el descuento del cliente: ")
        
        cliente= Cliente(nombre, apellido, rut, descuento)
        print("cliente creado:", cliente)
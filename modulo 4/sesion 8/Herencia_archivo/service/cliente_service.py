from modelo.cliente import Cliente

class ClienteService:
    #atributo que cargue una lista
    def __init__(self) -> None:
        self._cliente = self.load_clientes()#poner self porque constructor se construye cone el
    #metodo cargando archivo: lectura y creacion si archivo no existe
    def load_clientes(self):
        try:
            with open("clientes.txt", "r") as file:
                clientes=file.readlines()
        except FileNotFoundError:
            clientes=[]
            with open("clientes.txt", "w") as file:
                file.writelines(clientes)
        return clientes
    #escritura sobre archivo de la lista de clientes
    def save_clientes(self):
        with open("clientes.txt", "w") as file:
            for cliente in self._cliente:
                file.write(str(cliente))
    
    
    #metodo para crear clientes
    def crear_cliente(self):
        nombre= input ("ingrese nombre de cliente: ")
        apellido= input ("ingrese apellido de cliente: ")
        rut= input("ingrese rut de cliente: ")
        descuento =input("ingrese el descuento del cliente: ")
        
        cliente= Cliente(nombre, apellido, rut, descuento)
        print("cliente creado:", cliente)
        
        self._cliente.append(cliente)
        self.save_clientes()
    
    def list_clientes(self):
        print("Lista del clientes")
        for cliente in self._cliente:
            print(cliente)
            
    #BUSCAR CLIENTES POR RUT
    def get_cliente_by_rut(self, rut):
       
        for cliente in self._cliente:
            if cliente.rut == rut:
                return cliente
        return None
   
   #para editar el cliente
    def edit_cliente(self):
        rut = input("Ingrese rut de cliente a modificar: ")
        for cliente in self._cliente:
            if cliente.rut == rut:
                print("Cliente encontrado: ")
                cliente.nombre = input("ingrese nuevo nombre: ")
                cliente.apellido = input("Ingrese nuevo apellido")
                cliente.descuento =input("Ingrese el descuento: ")
                self.save_clientes()
                print("Cliente editado exitosamente", cliente)
        print("Cliente no encontrado")
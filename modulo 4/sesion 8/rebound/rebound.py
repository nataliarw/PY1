"""Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el archivo, debe reflejar un mensaje que especifica que ya se 
encuentra el archivo previamente creado.  
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente: """
#creamos archivo

def crear_archivo():
    try:
        file= open("informacion.dat", "x")
        file.close()
    except FileExistsError:
        print("Error: El archivo ya existe")
    except Exception as e:
        print("Error: ", e)
        
crear_archivo()

"""Partiendo de la actividad realizada en el Rebound Exercises,
construya una función que lea el contenido del 
archivo informacion.dat. """



def crear_archivo():
    try:
        file= open("informacion.dat", "x")
        file.close()
    except FileExistsError:
        print("Error: El archivo informacion.dat ya existe. Ha sido creado previamente")
    except Exception as e:
        print("Error: ", e)

def leer_archivo():
    try:
        with open ("informacion.dat", "r") as file:
           datos= file.readlines()
           for linea in datos:
               print(linea, end="")
    except FileNotFoundError:
        print("archivo no encontrado")
        
def escribir_archivo(lista):
    try:
        with open("informacion.dat", "w", encoding="UTF-8") as file:
            for dato in lista:
                file.write(dato+ "\n")
                
    except FileNotFoundError:
        print("no se ha encontrado el archivo")

lista = ["Datos de información en la línea 1", "Datos de información en la línea 2",  "Datos de información en la línea 3",
"Datos de información en la línea 4", 
"Datos de información en la línea 5"]       
crear_archivo()
escribir_archivo(lista)
leer_archivo()
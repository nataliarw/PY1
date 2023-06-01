"agregar contenido a archivo existente informacion.dat"
"""Hola Mundo  Este en una nueva línea en el archivo agregando 
la segunda línea del archivo finalizando la línea agregada """
# def agregar_info_al_archivo():
#     try:
#         file= open("informacion.dat", "a")
#         file.write("Hola Mundo \n Este en una nueva línea en el archivo \n agregando la segunda línea del archivo finalizando la línea agregada")
#         file.close()
#     except FileExistsError:
#         print("Error: El archivo ya existe")
#     except Exception as e:
#         print("Error: ", e)
        
# agregar_info_al_archivo()

def agregar_info_al_archivo(texto):
    try:
        with open ("informacion.dat", "a", encoding="utf-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: ARCHIVO NO ENCONTRADO")
    except Exception as e:
        print("ERROR: ", e)
        
agregar_info_al_archivo("Hola Mundo")
agregar_info_al_archivo("Este en una nueva línea en el archivo")
agregar_info_al_archivo("finalizando la línea agregada")
        
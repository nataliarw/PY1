usuarios= {"001": "Marca", "002": "Monica", "003": "Jacob"}
id_usuario ="004"
mensaje= "la clave 004 no esta en el diccionario"

# try:
#     print(usuarios[id_usuario])
    
# except KeyError:
#     print(mensaje)
# usuarios[id_usuario]=None

# print(usuarios)

def funcion(usuarios, id_usuario):
    try:
        print(usuarios[id_usuario])
    
    except KeyError:
        print(mensaje)
    usuarios[id_usuario]=None
    
funcion(usuarios, id_usuario)
print(usuarios)
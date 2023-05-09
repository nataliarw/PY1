# EJERCICIO DE CONSOLIDACION MODULO 3
# Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos.
# Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), 
# que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.  
# Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista. Finalmente, i
# mprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, 
# los nombres de los científicos, y los restantes. 


#OPCION CON LISTAS
# se declara la lista original
lista_completa = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
# se separa en las listas solicitadas
lista_magos = [lista_completa[0], lista_completa[2], lista_completa[5]]
lista_cientificos = [lista_completa[1],lista_completa[3], lista_completa[6]]

lista_otros = [lista_completa[4], lista_completa[7], lista_completa[8]]
# string a agregar en cada miembto de la lista magos
agregado= "El Gran "

# define funcion para agregar "el gran" a cada mago
def hacer_grandioso(lista_magos):
    grandes_magos = []
    for i in lista_magos:
        grandes_magos.append(agregado + i)
    return grandes_magos
        

# define funcion para imprimir todo lo solicitado
def imprimir_nombres():
    print('==> Lista Completa')
    for i in lista_completa:
        print(i)
    print('==> Lista Magos')
    for i in hacer_grandioso(lista_magos):
        print(i)
    print('==> Lista Cientificos')
    for i in lista_cientificos:
        print(i)
    print('==> Lista Otros')
    for i in lista_otros:
        print(i)
# imprime por consola lo solicitado, en el orden indicado
imprimir_nombres()


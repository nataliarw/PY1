# Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:  1 
# Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:   
# Si el primer número de la sublista es cero, omitir la impresión de toda la sublista. • 
# Si existe un cero en cualquier otra posición, omitir solo la impresión del cero. 

listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]] 


for lista in listas:
    if lista[0] == 0:
        listas.remove(lista)
    # print(listas)

for i, lista in enumerate(listas): 
    if lista[1] == 0:
        listas[i].remove(lista[1])
        
for i, lista in enumerate(listas): 
    if lista[-1] ==0:
        listas[-1].remove(lista[-1])

print(listas)
    



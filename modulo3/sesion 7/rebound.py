# Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero. 

numero= [10,15,26,0,48,7,3,55,63,70]

def parimpar(numero):
    for i in numero:
        if  i==0:
            print (f"{i} es cero")
        elif i % 2 ==0:      
            print (f"{i} es numero par")
        else:
            print (f"{i} es numero impar") 
            
parimpar(numero)
        
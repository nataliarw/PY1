lista =[3,5,2,8,1,10]
i = 0
# while i < len(lista):
#     if lista[i]% 2 ==0:
#         print(f"el primer numero par de la lista es {lista[i]}")
#         break
#     i = i +1
# else:
#     print("no hay numeros pares")
    
# calcular la suma de los numeros con ehilr
# resultado = 0
# while i< len(lista):
#     resultado = resultado +lista[i] #suma += lista[i]
#     i=i+1
# print(resultado)
#  ENCONTRAR EL NUMERO MAYOR DE UNA LISTA 
juego = [45, 23, 67, 89, 120, 45, 78, 90]
num = menor =juego[0]
repetido =[]
for i in juego:
    if i >num:
        num = i
    if i < menor:
        menor = i
    if juego.count(i) > 1 and i  not in repetido:
       repetido.append(i)
print(num, menor)
print(repetido)
print(max(juego))

precios= [25.50, 12.30, 36.40,9.75,15.20]
descuento =[]
for i in precios:
    i = i -(i*0.1)
    descuento.append(i)
    
print(sum(descuento))
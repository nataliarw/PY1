'''
las tuplas se definen con o sin parentesis, si esta vacia, 
debe ser con parentesis
'''
tupla =()
# o bien
tupla = tuple()

tupla = ("jose", "maria", 56, 4.2)
print(type(tupla))

print(tupla.count("jose"))

print(f"E1 elemento 31 su cuenta es {tupla.count(56)}") #1
print("E1 elemento 31 su cuenta es: {}".format(tupla.count("jose")))
print(tupla[1:2])

set_datos = set({10, 20, 30, 4, 8})
my_set ={} #se declara como direccionario cuando esta vacio

print (type(set_datos))
print (len(set_datos))

# agredar elementos a un set
set_datos.add(94)
# my_set no nos deja add un vacio, hay que igualarlo a set, por lo que no conviene dejarlo vacio
print(set_datos)
# update permite de mas de uno
set_datos.update({4,7,29})

# buscar elementos en un set, devuelve una condicional
print(10 in set_datos)
# remover el elemento
set_datos.remove(94)
# del borra la variable  clear los elementos
set2=(3,6,8,23)
set_datos = set_datos.union(set2) #tb esta diferencia e interceccion
print(set_datos)

a = {1, 2, 3, 4}
b = {1, 2, 5, 7} 
c = a & b
print(c)
print(type(a))


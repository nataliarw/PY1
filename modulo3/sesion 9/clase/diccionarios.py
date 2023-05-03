diccionario =dict()
otro_dicc= {}

otro_dict ={
    "nombre" : "Natalia",
    "apellido" :"Romanini",
    "direccion" : {
        "calle" : "Avenida Serrano", 
        "numero" : "567",
        "ciudad": "Santiago"
        }
}
print(otro_dict)
print(otro_dict["nombre"])
print("apellido" in otro_dict) #buscando una clave
print("Romanini" in otro_dict["apellido"]) #buscar un valor en una clave
# insertar un valor en una clave
otro_dict["nombre"] = "Andrea"
print(otro_dict)
otro_dict["direccion"]["numero"] = "679"
# eliminar elemento
del otro_dict["direccion"]["ciudad"]
# funcion items nos da las tuplas
print(otro_dict.items())
# agregar una clave y valor
otro_dict["edad"] ="40"
print(otro_dict)
print(otro_dict["direccion"])
# para saber las claves
# otro_dict = dict.fromkeys() 
# puedo poner una tupla dentro de esto para que se conviertan en las keys
arroz = dict.fromkeys(["a", "b", "c"], "ana")
print(arroz)
claves = ["a", "b", "c"] 
valores = [1, 2, 3] 
nuevo_diccionario = {} for i in range(len(claves)): nuevo_diccionario[claves[i]] = valores[i] print(nuevo_diccionario)
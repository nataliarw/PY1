"""
Diseñe una nueva clase de excepción definida 
por el usuario, que gestione la entrada del 
valor de una variable salario, y la misma se 
encuentre entre los valores de 1000 y 2000; 
de lo contrario, se lanza una excepción que 
refleja que el salario no se encuentra en el 
rango de 1000 y 2000. 

"""
class RangoSalarioError(Exception):
    pass

def probando_salario():
    try:
        salario = int(input("Ingrese el salario: "))
        if salario<=1000 or salario >=2000:
            raise RangoSalarioError("Salario no se encuentra en el rango entre 1000 y 2000")
        else:
            print("Su salario de ", salario, "se encuentra en el rango de 1000 a 2000")
    except RangoSalarioError as e:
        print("deberia pedir un aumento porque", e)
        
probando_salario()
    
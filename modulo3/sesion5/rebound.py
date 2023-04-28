n = int(input("Ingrese un numero: "))
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n<0:
       resultado ="El número para factorizar debe ser positivo"
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

resultfactorial = factorial(n)
print(f"el factorial de {n} es {resultfactorial}")
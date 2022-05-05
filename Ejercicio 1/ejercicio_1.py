# Ejercicio 1
#Enunciado del ejercicio:
#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros

#  y otra función que calcule el área de un círculo recibiendo el radio del mismo.
# Formula: A = PI * r ** 2

import math
# Funcion para para el aerea de un triangulo
def area_trinagulo(altura, base):
    area = (altura * base)/2
    return area

print(f"El area del triangulo es: {area_trinagulo(8, 2)} ")   
print()


# Funcion para para el aerea de un circulo
def area_circulo(radio):
   area = math.pi * radio ** 2
   return area

print(f"El area del circulo es {area_circulo(1.5)}")   

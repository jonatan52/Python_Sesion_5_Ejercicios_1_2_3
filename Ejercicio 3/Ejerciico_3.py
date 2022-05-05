# Ejercicio 3
# Enunciado del ejercicio:
# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return f"El año {anio} es bisiesto"
    else:
        return f"El año {anio} no es bisiesto" 
print(bisiesto(2020))        
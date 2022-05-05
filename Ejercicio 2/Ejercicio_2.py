# Ejercicio 2
# Enunciado del ejercicio:
# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        return f"El numero {numero} es primo"
    else:
        return f"El numero {numero} no es primo"
    
print(es_primo(19))    
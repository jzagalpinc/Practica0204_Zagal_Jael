# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = list(range(1, 11))

numeros_inversos = numeros[::-1]
print(", ".join(map(str, numeros_inversos)))
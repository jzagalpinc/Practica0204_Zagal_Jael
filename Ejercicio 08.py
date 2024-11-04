# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra = input("Introduce una palabra o frase: ")
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo")
else:
    print(f"'{palabra}' no es un palíndromo")
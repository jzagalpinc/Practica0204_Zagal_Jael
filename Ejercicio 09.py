# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduce una palabra: ").lower()
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

print("\nFrecuencia de cada vocal:")
for vocal, cantidad in vocales.items():
    print(f"La vocal {vocal}: aparece {cantidad} veces")
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros_loteria = []

print("Introduce los 6 números ganadores de la lotería primitiva (1-49):")
for i in range(6):
    while True:
        try:
            numero = int(input(f"Introduce el número {i+1}: "))
            if 1 <= numero <= 49:
                if numero not in numeros_loteria:
                    numeros_loteria.append(numero)
                    break
                else:
                    print("Ese número ya fue introducido. Introduce otro número.")
            else:
                print("El número debe estar entre 1 y 49")
        except ValueError:
            print("Por favor, introduce un número válido")

numeros_loteria.sort()  # Ordenar de menor a mayor
print("\nLos números ganadores ordenados son:", numeros_loteria)
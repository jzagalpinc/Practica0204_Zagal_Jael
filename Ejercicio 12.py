# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_desviacion_tipica(numeros):
    media = calcular_media(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    varianza = suma_cuadrados / len(numeros)
    return varianza ** 0.5

while True:
    try:
        entrada = input("Introduce una lista de números separados por comas: ")
        numeros = [float(x.strip()) for x in entrada.split(',')]
        if len(numeros) > 0:
            break
        else:
            print("Por favor, introduce al menos un número")
    except ValueError:
        print("Error: Asegúrate de introducir números válidos separados por comas")

media = calcular_media(numeros)
desviacion = calcular_desviacion_tipica(numeros)

print(f"\nLista de números: {numeros}")
print(f"Media: {media:.2f}")
print(f"Desviación típica: {desviacion:.2f}")
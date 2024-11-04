# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = list("abcdefghijklmnñopqrstuvwxyz")

for i in range(len(abecedario)-1, -1, -1):
    if (i + 1) % 3 == 0:
        abecedario.pop(i)

print("Abecedario sin letras en posiciones múltiplos de 3:")
print(abecedario)
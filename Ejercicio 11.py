#Escribir un programa que almacene las matrices: en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[-1, 0],
     [0, 1],
     [1, 1]]

def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

C = multiplicar_matrices(A, B)

print("Resultado de la multiplicación A × B:")
for fila in C:
    print(fila)

print("\nResultado en formato matriz:")
for fila in C:
    fila_str = "  ".join(f"{x:3}" for x in fila)
    print(f"[{fila_str}]")
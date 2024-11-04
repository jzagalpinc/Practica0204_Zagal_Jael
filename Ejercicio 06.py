# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspendidas = []

for subject in subjects:
    while True:
        try:
            nota = float(input(f"¿Qué nota has sacado en {subject}? "))
            if 0 <= nota <= 10:
                if nota < 5:
                    suspendidas.append(subject)
                break
            else:
                print("Por favor, introduce una nota entre 0 y 10")
        except ValueError:
            print("Error: Por favor, introduce un número válido")

if suspendidas:
    print("\nTienes que repetir estas asignaturas:")
    for subject in suspendidas:
        print(subject)
else:
    print("\n¡Felicidades! Has aprobado todas las asignaturas")
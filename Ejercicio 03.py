# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []

for subject in subjects:
    while True:
        try:
            score = float(input(f"¿Qué nota has sacado en {subject}? "))
            if 0 <= score <= 10:
                scores.append(score)
                break
            else:
                print("Por favor, introduce una nota entre 0 y 10")
        except ValueError:
            print("Error: Por favor, introduce un número válido")

print("\nRESULTADOS:")
for i in range(len(subjects)):
    print(f"En {subjects[i]} has sacado {scores[i]}")

media = sum(scores) / len(scores)
print(f"\nTu nota media es: {media:.2f}")
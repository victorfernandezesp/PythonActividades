""" Ejercicio 10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación
                    se compone de los siguientes porcentajes:

        * 55% del promedio de sus tres calificaciones parciales.

        * 30% de la calificación del examen final.

        * 15% de la calificación de un trabajo final.

       Este programa mediante una entrada por teclado de notas almacenadas en varias variables, realizara una serie de
       cálculos para adivinar la nota final y mediante un mensaje lo muestra por pantalla el resultado de la nota final.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
PESO_TRABAJO_FINAL = 0.15
PESO_EXAMEN_FINAL = 0.3
PESO_EXAMEN_PARCIALES = 0.55
print("Introduce la notas que se le pedirán a continuación ")
parcial1 = float(input("¡Introduce la calificación del parcial 1, por favor! "))
parcial2 = float(input("¡Introduce la calificación del parcial 2, por favor! "))
parcial3 = float(input("¡Introduce la calificación del parcial 3, por favor! "))
nota_exa_final = float(input("¡Introduce la calificación del examen final, por favor! "))
nota_trabajo_final = float(input("¡Introduce la calificación del trabajo final, por favor! "))

nota_parciales = ((parcial1 + parcial2 + parcial3) / 3)
nota_final = nota_parciales * PESO_EXAMEN_PARCIALES + nota_exa_final * PESO_EXAMEN_FINAL \
             + nota_trabajo_final * PESO_TRABAJO_FINAL

print(f" La nota final es de {nota_final:.2f}")
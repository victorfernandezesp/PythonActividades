""" 10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone
        de los siguientes porcentajes:

        * 55% del promedio de sus tres calificaciones parciales.

        * 30% de la calificación del examen final.

        * 15% de la calificación de un trabajo final.

       Este programa mediante una entrada por teclado de notas almacenadas en varias variables, realizara una serie de
       cálculos para adivinar la nota final y mediante un mensaje lo muestra por pantalla el resultado de la nota final.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce la notas que se le pedirán a continuación ")
parcial1 = float(input("¡Introduce la calificación del parcial 1, por favor! "))
parcial2 = float(input("¡Introduce la calificación del parcial 2, por favor! "))
parcial3 = float(input("¡Introduce la calificación del parcial 2, por favor! "))
exa_final = float(input("¡Introduce la calificación del examen final, por favor! "))
trabajo_final = float(input("¡Introduce la calificación del trabajo final, por favor! "))

porcentaje_parciales = ((parcial1 + parcial2 + parcial3) / 3) * 0.55
exa_final_porcentaje = exa_final * 0.3
trabajo_final_porcentaje = trabajo_final * 0.15
nota_final = round(porcentaje_parciales + exa_final_porcentaje + trabajo_final_porcentaje, 2)

print(" La nota final es de ", nota_final)
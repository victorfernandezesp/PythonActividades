# 9.Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de
# los siguientes porcentajes:
#
# 55% del promedio de sus tres calificaciones parciales.
#
# 30% de la calificación del examen final.
#
# 15% de la calificación de un trabajo final.
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
parcial1 = float(input("Introduce la nota del parcial numero 1 "))
parcial2 = float(input("Introduce la nota del parcial numero 2 "))
parcial3 = float(input("Introduce la nota del parcial numero 3 "))

exa_final = float(input("Introduce la nota del examen final "))

trabajo_final = float(input("Introduce la nota del trabajo final "))

# Realizamos las distintas operaciones
parciales = round((((parcial1 + parcial2 + parcial3)/3)*0.55), 2)
exa_final = round((exa_final*0.30), 2)
trabajo_final = round((trabajo_final*0.15), 2)

nota_final = parciales + exa_final + trabajo_final
# Mostramos por pantalla los resultados
print(" Su nota final es de :", nota_final)

""" 19. Escribir un programa para calcular la nota final de un estudiante, considerando que:

        cada respuesta correcta suma 5 puntos
        cada respuesta incorrecta suma -1 puntos
        cada respuesta en blanco suma 0 puntos.
        Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
        ¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas puedan
        cambiar en el futuro?

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te calcula la calificación de un examen teniendo en cuenta las respuestas correctas, en blanco "
      "y mal ")
correct = int(input("Introduce cuantas respuestas correctas tienes, por favor "))
void = int(input("Introduce cuantas respuestas en blanco tienes tienes, por favor "))
incorrect = int(input("Introduce cuantas respuestas incorrectas tienes, por favor "))

summation = correct + void + incorrect
total_points = summation * 5
final_mark = ((correct*5 - incorrect*-1)/total_points)*10

print(f" Tu nota ha sido de: {round(final_mark,2)} puntos")

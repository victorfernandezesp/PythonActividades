# 19. Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta correcta
# 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
correct = int(input("¿Cuantas respuestas correctas tienes? "))
null = int(input("¿Cuantas respuestas en blanco tienes tienes? "))
incorrect = int(input("¿Cuantas respuestas incorrectas tienes? "))


# Realizamos las distintas operaciones
correct = correct*5
null = null*0
incorrect = incorrect*-1

final_Mark = correct + null + incorrect

# Mostramos por pantalla los resultados
print(f" Tu resultado ha sido de: {final_Mark} puntos")

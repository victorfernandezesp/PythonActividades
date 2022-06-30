# 13. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna
# función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
import math

number1 = int(input("Introduce el numero 1 "))


# Realizamos las distintas operaciones
square = int(math.pow(number1, 2))
cube = int(math.pow(number1, 3))
# Mostramos por pantalla los resultados
print(f"El numero al cuadrado es {square} y el numero al cubo es {cube}")
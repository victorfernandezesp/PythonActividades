""" 13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna
        función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import math
import numpy as np
print("Este programa te dara la raíz cuadrada y cubica de un numero")
numero1 = int(input("¡Introduce el numero, por favor! "))

cuadrada = float(math.sqrt(numero1))
cubica = float(np.cbrt(numero1))

print("La raíz cuadrada de ", numero1, " es ", cuadrada, " y su cubica es ", cubica)
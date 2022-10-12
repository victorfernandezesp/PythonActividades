""" 12. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra
        la distancia entre ellos..

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import math
print("Este programa te dara la distancia entre 2 coordenadas")
x1 = int(input("¡Introduce la coordenada x1, por favor! "))
y1 = int(input("¡Introduce la coordenada y1, por favor! "))
x2 = int(input("¡Introduce la coordenada x2, por favor! "))
y2 = int(input("¡Introduce la coordenada y2, por favor! "))

distance = int(abs(math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))))

print(" La distancia entre las coordenadas es ", distance)
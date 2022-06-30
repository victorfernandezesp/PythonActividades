# 12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la
# distancia entre ellos.
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
import math

x1 = int(input("Introduce x1 "))
y1 = int(input("Introduce y1 "))
x2 = int(input("Introduce x2 "))
y2 = int(input("Introduce y2 "))

# Realizamos las distintas operaciones
distance = abs(math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)))
# Mostramos por pantalla los resultados
print(f"La distancia entre los puntos es: {distance}")
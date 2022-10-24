""" Ejercicio 10.
    Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

        exteriores
        tangentes exteriores
        secantes
        tangentes interiores
        interiores
        concéntricas
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import math

print("Este programa te el tipo de circunferencia que es ")

x1 = float(input("Introduce la coordenada x1: "))
y1 = float(input("Introduce la coordenada y1: "))
r1 = float(input("Introduce el radio r1: "))

x2 = float(input("Introduce la coordenada x2: "))
y2 = float(input("Introduce la coordenada y2: "))
r2 = float(input("Introduce el radio r2: "))

distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
if distance > (r1 + r2):
    print(f"Circunferencias exteriores")
elif (r1 + r2) > distance > abs(r1 - r2):
    print(f"Circunferencias secantes")
elif 0 < distance < abs(r1 - r2):
    print(f"Circunferencias interiores")
elif distance == (r1 + r2):
    print(f"Circunferencias tangentes exteriores")

elif distance == abs(r1 - r2):
    print(f"Circunferencias tangentes interiores")

elif distance == 0:
    print(f"Circunferencias concéntricas")
else:
    print(f"Esta situación es imposible")

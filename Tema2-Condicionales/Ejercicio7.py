# 7. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir
# tres cosas:
# Author: Victor Fernandez España

# Introducimos por teclado el número con el que vamos a trabajar
import math

base = int(input("Introduce una base por teclado: "))
exponente = int(input("Introduce una base por teclado: "))
print(f"-----------------------------------------------------------------")

# Realizamos las distintas operaciones
if exponente > 1:
    resultado = math.pow(base, exponente)
    # Mostramos por pantalla los resultados
    print(f"El resultado es {resultado}")

elif exponente < 0:
    resultado = 1/(math.pow(base, abs(exponente)))
    print(f"El resultado es {resultado}")

else:
    print(f"El resultado es 1 ")

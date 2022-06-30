# 11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que
# el resultado sea siempre positivo).
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
numero1 = int(input("Introduce el primer numero "))
numero2 = int(input("Introduce el segundo numero "))

# Realizamos las distintas operaciones
distancia = abs(numero1-numero2)

# Mostramos por pantalla los resultados
print("La distancia absoluta entre los números es: ", distancia)
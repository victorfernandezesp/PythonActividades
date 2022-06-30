# 5. Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta
# que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
age1 = int(input("Introduce la edad 1 y te dire si es mayor que la 2: "))
age2 = int(input("Introduce la edad 2 y te dire si es mayor que la 1: "))
print(f"-----------------------------------------------------------------")

# Realizamos las distintas operaciones
if age1 > age2:
    # Mostramos por pantalla los resultados
    print(f" La edad 1 es mayor que el 2 ")
elif age1 == age2:
    # Mostramos por pantalla los resultados
    print(f"Ambos tienen la misma edad ")

else:
    # Mostramos por pantalla los resultados
    print(f" La edad 2 es mayor que el 1 ")

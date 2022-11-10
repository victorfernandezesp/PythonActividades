"""
    Ejercicio 6:
        Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array.
        El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array
        (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si
        es necesario.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange
array_ordena = []
array_aux_pares = []
array_aux_impares = []

for i in range(20):
    num_random = randrange(0, 100)
    array_ordena.append(num_random)
print("El array antes de ordenarlo:")
print(f"{array_ordena}")
for j in array_ordena:
    if j % 2 == 0:
        array_aux_pares.append(j)
    else:
        array_aux_impares.append(j)

array_aux_pares.sort()
array_aux_impares.sort()
array_ordena.clear()
array_ordena.extend(array_aux_pares)
array_ordena.extend(array_aux_impares)
print("El array después de ordenarlo:")
print(f"{array_ordena}")
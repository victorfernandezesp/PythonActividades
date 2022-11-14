"""
    Ejercicio 1:

        Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
        columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se
        tratara. La suma total debe aparecer en la esquina inferior derecha.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

# Vamos a realizar una suma de un vector

vector = []
suma = 0

cant_num = int(input("Cuantos numeros va a contener el array que quieres que sume?:     "))
for x in range(cant_num):
    auxiliar = int(input("Introduce el numero:      "))
    vector.append(auxiliar)

for x in vector:
    print(f"{sum(vector)}")
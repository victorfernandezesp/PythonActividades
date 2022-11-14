"""
    Vamos a realizar una suma de un vector

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

vector = []
suma = 0

cant_num = int(input("Cuantos numeros va a contener el array que quieres que sume?:     "))
for x in range(cant_num):
    auxiliar = int(input("Introduce el numero:      "))
    vector.append(auxiliar)

for x in vector:
    print(f"{sum(vector)}")
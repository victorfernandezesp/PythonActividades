"""
    Ejercicio 4:

        Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las
        palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

print("Este programa saca el minimo y el maximo de los valores de un array cuyos valores se introducen por teclado.")
array_ordena = []
for i in range(3):
    num_introduce = int(input("Introduce un numero para almacenarlo en el array: "))
    array_ordena.append(num_introduce)

array_ordena.sort()
print(f"El numero minimo del array es {array_ordena[0]}")
array_ordena.reverse()
print(f"El numero maximo del array es {array_ordena[0]}")

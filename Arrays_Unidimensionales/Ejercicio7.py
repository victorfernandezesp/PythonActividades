"""
    Ejercicio 7:

        Escribe un programa que lea 15 números por teclado y que los almacene en un array.
        Rota los elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1
        a la 2, etc. El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra
        el contenido del array.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
NUMERO_DE_ELEMENTOS = 15
array_inicio = []
array_auxiliar = []

for i in range(NUMERO_DE_ELEMENTOS):
    numero = input("Escribe un numero: ")
    array_inicio.append(numero)

array_auxiliar.append(array_inicio.pop())
for j in array_inicio:
    array_auxiliar.append(j)

array_inicio = array_auxiliar
print(f"{array_inicio}")
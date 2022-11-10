"""
    Ejercicio 4:

        Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la
        mala suerte son el resto: el 0, el 1, el 2, el 4, el 5 y el 6. Un número es afortunado si contiene más
        números de la suerte que de la mala suerte. Realiza un programa que diga si un número introducido
        por el usuario es afortunado o no.
        Ejemplo 1: Introduzca un número: 772
        El 772 es un número afortunado.
        Ejemplo 2: Introduzca un número: 7720
        El 7720 no es un número afortunado.
        Ejemplo 3: Introduzca un número: 43081
        El 43081 no es un número afortunado.
        Ejemplo 4: Introduzca un número: 888
        El 888 es un número afortunado.
        Ejemplo 5: Introduzca un número: 1234
        El 1234 no es un número afortunado.
        Ejemplo 6: Introduzca un número: 6789
        El 6789 es un número afortunado.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

SUMA_POR_NUMERO_NO_AFORTUNADO = 1

SUMA_POR_NUMERO_AFORTUNADO = 1

ERROR_NUMERO_NO_DIGITOS = 1

num_afortunados = "3789"
num_no_afortunados = "012456"

contador_afortunados = 0
contador_no_afortunados = 0

num_introducido = input("Introduzca un número y te dire si es afortunado o no: ")
if not num_introducido.isdigit():
    print("ERROR. Tu número no debe contener otros caracteres ajenos a los digitos", file=sys.stderr)
    sys.exit(ERROR_NUMERO_NO_DIGITOS)

for numero_en_posicion in num_introducido:
    if numero_en_posicion in num_afortunados:
        contador_afortunados += SUMA_POR_NUMERO_AFORTUNADO
    else:
        contador_no_afortunados += SUMA_POR_NUMERO_NO_AFORTUNADO

if contador_no_afortunados >= contador_afortunados:
    print(f"El {num_introducido} NO es un número afortunado.")
else:
    print(f"El {num_introducido} es un número afortunado.")

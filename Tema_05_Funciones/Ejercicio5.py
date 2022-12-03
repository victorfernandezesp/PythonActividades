"""
    Ejercicio 5:
        Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva
        en una cadena de caracteres.

        Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

        Utiliza esta función en un programa para comprobar que funciona bien.
        Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys


def convertir_numeros_a_palotes(numero):
    contador_guiones = 1
    concatenacion_total = ""
    longitud_num = len(numero)
    guion = "-"

    for digito in numero:
        digito = int(digito)
        palos = "|" * digito
        concatenacion_parcial = palos
        if contador_guiones < longitud_num:
            concatenacion_parcial += guion
            contador_guiones += 1
        concatenacion_total += concatenacion_parcial

    return concatenacion_total


ERROR_NUMERO_NO_ENTERO_POSITIVO = 1

num_entero = input("Por favor, introduzca un número entero positivo: ")
if not num_entero.isdigit():
    print("ERROR. El número introducido solo acepta valores positivos, introduce solo enteros positivos",
          file=sys.stderr)
    sys.exit(ERROR_NUMERO_NO_ENTERO_POSITIVO)

print(f"{convertir_numeros_a_palotes(num_entero)}")

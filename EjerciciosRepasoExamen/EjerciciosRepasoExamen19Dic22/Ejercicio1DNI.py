"""
    Ejercicio 1:

        Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y la letra es correcta.
        Para calcular la letra se divide el número entre 23 y el resto indica la posición de la cadena de letras:
        "TRWAGMYFPDXBNJZSQVHLCKE"

        CON FUNCIONES

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

ERROR_SIN_LETRA = 3

ERROR_8_DIGITOS = 2

ERROR_LONGITUD_DISTINTO_A_9 = 1


def introduce_dni():
    nif = input("Introduce el DNI, recuerda que tiene que tener 9 caracteres y la letra debe ser la correcta:   ")
    if len(nif) != 9:
        print(f"ERROR. Tu DNI tiene que tener una longitud de 9 caracteres", file=sys.stderr)
        sys.exit(ERROR_LONGITUD_DISTINTO_A_9)

    if not nif[:8].isdigit():
        print(f"ERROR. Tu DNI tiene que tener 8 números", file=sys.stderr)
        sys.exit(ERROR_8_DIGITOS)

    if not nif[8].isalpha():
        print(f"ERROR. Tu DNI tiene que tener 1 letra", file=sys.stderr)
        sys.exit(ERROR_SIN_LETRA)

    return nif


def comprueba_dni(nif):
    letras_posibles = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros_nif = int(nif[:8])
    letra_nif = nif[8]

    posicion_letra = numeros_nif % 23
    if letras_posibles[posicion_letra] == letra_nif:
        print("Su DNI es verdadero.")
    else:
        print("Su DNI es falso, esta usted detenido.")


dni = introduce_dni()
comprueba_dni(dni)

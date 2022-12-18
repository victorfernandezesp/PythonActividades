"""
    Ejercicio 1:

        Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y la letra es correcta.
        Para calcular la letra se divide el número entre 23 y el resto indica la posición de la cadena de letras:
        "TRWAGMYFPDXBNJZSQVHLCKE"

        VERSION CON BUCLE

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

ERROR_LETRA_DNI = 3

ERROR_CARACTERES_NUMERICOS = 2

ERROR_LONGITUD_DISTINTO_A_9 = 1

conjunto_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
dni_comprobacion = False
while True:
    dni = input("Escribe tu DNI: ").upper()
    if len(dni) != 9:
        print(f"ERROR. Tu DNI tiene que tener una longitud de 9 caracteres", file=sys.stderr)
        sys.exit(ERROR_LONGITUD_DISTINTO_A_9)
    num_dni = dni[:8]
    if not num_dni.isdigit():
        print(f"ERROR. Tu DNI tiene que tener 8 primeros caracteres numéricos", file=sys.stderr)
        sys.exit(ERROR_CARACTERES_NUMERICOS)
    letra_dni = dni[8]
    if not letra_dni.isalpha():
        print(f"ERROR. Tu DNI tiene que tener una letra alfabética al final", file=sys.stderr)
        sys.exit(ERROR_LETRA_DNI)

    posicion = int(num_dni) % 23
    letra = conjunto_letras[posicion]

    if letra != letra_dni:
        print(f"Su DNI {dni} no es correcto, vuelva a intentarlo")
        continue
    else:
        print(f"El DNI {dni} es verdadero.")
        break

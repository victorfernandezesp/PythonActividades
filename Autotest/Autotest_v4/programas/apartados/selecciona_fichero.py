"""
    Autotest V4:

        2. Seleccionar fichero de test.

        Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
        La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.
        Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
        Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Autotest.Autotest_v4.programas.apartados.crear_fichero_test import pregunta_archivo


def selecciona_fichero():
    while True:
        extension, nombre_fichero = pregunta_archivo()
        if ".json" in extension or ".xml" in extension:
                break
        else:
            print("Selecciona un archivo .xml o . json")
            continue

    return nombre_fichero

if __name__ == '__main__':
    selecciona_fichero()
"""
    Autotest V4:
    Crear un programa con las siguientes opciones:
        1. Crear fichero de test.

        Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
        La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.
        Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
        Finalmente se creará el fichero correspondiente.


        2. Seleccionar fichero de test.

        Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
        La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.
        Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
        Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.


        3. Añadir pregunta al test.

        Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
        Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
        Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción
        es que están bien.
        Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
        Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en
        el fichero.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

import sys

from Autotest.Autotest_v4.programas.apartados.anadir_preguntas import anadir_preguntas
from Autotest.Autotest_v4.programas.apartados.crear_fichero_test import crear_fichero_test
from Autotest.Autotest_v4.programas.apartados.selecciona_fichero import selecciona_fichero
from programas.menu.menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu_anade_pregunta = Menu("PREGUNTORIO",
             "Crear fichero de test.",
             "Seleccionar fichero de test.",
             "Añadir pregunta al test."
                )
fichero = ""

while True:
    option = menu_anade_pregunta.escoger()
    match option:

        case 1:
            crear_fichero_test()
        case 2:
            fichero = selecciona_fichero()
            fichero_1 = open(fichero, 'wt')
        case 3:
            try:
                fichero_2 = open(fichero, 'wt')
            except FileNotFoundError:
                print("Fichero no seleccionado")
            except PermissionError:
                print("No tienes permisos para abrir este archivo")

            anadir_preguntas(fichero_2)

        case 4:
            print("¡Hasta la próxima ^_^!")
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
        case _:
            print("Ha introducido una opcion incorrecta, vuelva a intentarlo.")
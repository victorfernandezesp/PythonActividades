"""
    Autotest V4:
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

def anadir_preguntas(fichero_donde_se_anaden_preguntas):
    print(fichero_donde_se_anaden_preguntas)


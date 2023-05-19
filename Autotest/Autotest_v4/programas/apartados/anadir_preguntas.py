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
import json
import os as OS
import sys
import xml.etree.ElementTree as ET
from Autotest.Autotest_v4.question import Question


def comprueba_pregunta(titulo_pregunta, enunciado_pregunta, opciones, puntuacion):
    try:
        pregunta_prueba = Question(titulo_pregunta, enunciado_pregunta, opciones, puntuacion)
    except ValueError:
        print("El formato de la pregunta no es correcto.", file=sys.stderr)
        sys.exit(1)


def anadir_preguntas(extension_del_fichero, fichero_donde_se_anaden_preguntas):

    if extension_del_fichero == ".json":
        titulo_pregunta = input("Introduce el título de la pregunta:    ")
        puntuacion = int(input("Introduce el peso de la pregunta:   "))
        enunciado_pregunta = input("Introduce el enunciado de la pregunta:  ")
        opciones = []
        opciones_en_formato_json = []
        for opcion in range(4):
            opcion_de_pregunta = input("Introduce una opción de la pregunta:    ")
            while True:
                valor_de_pregunta = input("Introduce el valor de la opción de la pregunta:    ")
                try:
                    comprueba_valor_de_pregunta_es_float = float(valor_de_pregunta)
                except:
                    print("Introduce un número real")
                    continue
                opciones.append((opcion_de_pregunta, float(valor_de_pregunta)))
                opciones_en_formato_json.append({"opcion": opcion_de_pregunta, "valor": float(valor_de_pregunta)})
                break

        comprueba_pregunta(titulo_pregunta, enunciado_pregunta, opciones, puntuacion)
        todas_las_preguntas = []
        pregunta = {
            "nombre": titulo_pregunta,
            "enunciado": enunciado_pregunta,
            "opciones": opciones_en_formato_json,
            "puntuacion_base": puntuacion}

        if OS.stat(fichero_donde_se_anaden_preguntas).st_size > 0:
            with open(fichero_donde_se_anaden_preguntas, 'rt', encoding='utf-8') as f:
                preguntas = json.load(f)
            todas_las_preguntas = preguntas
        todas_las_preguntas.append(pregunta)

        with open(fichero_donde_se_anaden_preguntas, 'wt') as f:
            json.dump(todas_las_preguntas, f, indent=1)


    else:

        tree = ET.parse(fichero_donde_se_anaden_preguntas)
        root = tree.getroot()

        titulo_pregunta = input("Introduce el título de la pregunta:    ")
        puntuacion = input("Introduce el peso de la pregunta:   ")
        enunciado_pregunta = input("Introduce el enunciado de la pregunta:  ")
        lista_opciones = []
        opciones_en_formato_xml = []

        pregunta = ET.Element('pregunta', {'nombre': titulo_pregunta, 'puntuacion_base': puntuacion})
        enunciado = ET.SubElement(pregunta, 'enunciado')
        enunciado.text = enunciado_pregunta
        opciones = ET.SubElement(pregunta, 'opciones')

        for opcion in range(4):
            opcion_de_pregunta = input("Introduce una opción de la pregunta:    ")
            while True:
                valor_de_pregunta = input("Introduce el valor de la opción de la pregunta:    ")
                try:
                    comprueba_valor_de_pregunta_es_float = float(valor_de_pregunta)
                except:
                    print("Introduce un número real")
                    continue
                opcion_n = ET.SubElement(opciones, 'opcion', {'valor': valor_de_pregunta})
                opcion_n.text = opcion_de_pregunta
                lista_opciones.append((opcion_de_pregunta, float(valor_de_pregunta)))
                opciones_en_formato_xml.append({"opcion": opcion_de_pregunta, "valor": valor_de_pregunta})
                break

        comprueba_pregunta(titulo_pregunta, enunciado_pregunta, lista_opciones, int(puntuacion))
        root.append(pregunta)
        ET.indent(root, space='    ')
        tree.write(fichero_donde_se_anaden_preguntas, encoding='unicode')
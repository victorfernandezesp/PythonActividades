"""
        Ejercicio Autotest V1.2:

            Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
            Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import xml.etree.ElementTree as ET
import sys

from Autotest.Autotest_v3.question import Question

def main():
    nombre_de_fichero = sys.argv[1]
    comprueba_existe_fichero(nombre_de_fichero)

    archivo = ET.parse(nombre_de_fichero)
    root = archivo.getroot()

    for i in range(len(root)):
        nombre = root[i].get("nombre")
        enunciado = root[i][0].text

        opcion1 = root[i][1][0].text
        valor_opcion1 = root[i][1][0].get("valor")

        opcion2 = root[i][1][1].text
        valor_opcion2 = root[i][1][1].get("valor")

        opcion3 = root[i][1][2].text
        valor_opcion3 = root[i][1][2].get("valor")

        opcion4 = root[i][1][3].text
        valor_opcion4 = root[i][1][3].get("valor")

        enunciado, nombre, opcion1, opcion2, opcion3, opcion4, valor_opcion1, valor_opcion2, valor_opcion3, valor_opcion4 =\
            guarda_parametros_sin_tabulaciones_ni_saltos_de_lineas(enunciado, nombre, opcion1, opcion2, opcion3, opcion4, valor_opcion1, valor_opcion2, valor_opcion3, valor_opcion4)

        opciones = ([(opcion1, float(valor_opcion1)), (opcion2, float(valor_opcion2)), (opcion3, float(valor_opcion3)), (opcion4, float(valor_opcion4))])
        pregunta_usuario = Question(nombre, enunciado, opciones, 1)
        pregunta_usuario.muestra_pregunta()
        pregunta_usuario.respuesta_usuario()


def guarda_parametros_sin_tabulaciones_ni_saltos_de_lineas(enunciado, nombre, opcion1, opcion2, opcion3, opcion4,
                                                           valor_opcion1, valor_opcion2, valor_opcion3, valor_opcion4):
    nombre = quita_salto_de_linea_y_espacios_innecesarios(nombre)
    enunciado = quita_salto_de_linea_y_espacios_innecesarios(enunciado)
    opcion1 = quita_salto_de_linea_y_espacios_innecesarios(opcion1)
    valor_opcion1 = quita_salto_de_linea_y_espacios_innecesarios(valor_opcion1)
    opcion2 = quita_salto_de_linea_y_espacios_innecesarios(opcion2)
    valor_opcion2 = quita_salto_de_linea_y_espacios_innecesarios(valor_opcion2)
    opcion3 = quita_salto_de_linea_y_espacios_innecesarios(opcion3)
    valor_opcion3 = quita_salto_de_linea_y_espacios_innecesarios(valor_opcion3)
    opcion4 = quita_salto_de_linea_y_espacios_innecesarios(opcion4)
    valor_opcion4 = quita_salto_de_linea_y_espacios_innecesarios(valor_opcion4)
    return enunciado, nombre, opcion1, opcion2, opcion3, opcion4, valor_opcion1, valor_opcion2, valor_opcion3, valor_opcion4


def quita_salto_de_linea_y_espacios_innecesarios(parametro):
    parametro = parametro.replace('\n', '')
    parametro = parametro.replace('  ', '')

    return parametro


def comprueba_existe_fichero(fichero):
    try:
        fichero_comprueba = open(fichero, 'rt')
        fichero_comprueba.close()
    except FileNotFoundError:
        print("El archivo no existe.")
        sys.exit(1)
if __name__ == '__main__':
    main()

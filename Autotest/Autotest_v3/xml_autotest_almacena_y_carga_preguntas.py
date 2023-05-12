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
        if nombre is None:
            nombre = ""
        puntuacion_base = root[i].get("puntuacion_base")
        enunciado = root[i][0].text.strip()

        opcion1 = root[i][1][0].text.strip()
        valor_opcion1 = root[i][1][0].get("valor")

        opcion2 = root[i][1][1].text.strip()
        valor_opcion2 = root[i][1][1].get("valor")

        opcion3 = root[i][1][2].text.strip()
        valor_opcion3 = root[i][1][2].get("valor")

        opcion4 = root[i][1][3].text.strip()
        valor_opcion4 = root[i][1][3].get("valor")

        opciones = ([(opcion1, float(valor_opcion1)), (opcion2, float(valor_opcion2)), (opcion3, float(valor_opcion3)), (opcion4, float(valor_opcion4))])
        pregunta_usuario = Question(nombre, enunciado, opciones, int(puntuacion_base))
        pregunta_usuario.muestra_pregunta()
        pregunta_usuario.respuesta_usuario()
    pregunta_usuario.imprimir_puntuacion_final()


def comprueba_existe_fichero(fichero):
    try:
        fichero_comprueba = open(fichero, 'rt')
        fichero_comprueba.close()
    except FileNotFoundError:
        print("El archivo no existe.")
        sys.exit(1)
if __name__ == '__main__':
    main()
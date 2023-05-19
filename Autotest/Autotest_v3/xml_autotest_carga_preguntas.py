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
        puntos = root[i].get("puntuacion_base")

        enunciado = root[i][0].text.strip()
        opciones = root[i][1]
        tuplas_opciones = []
        for j in range(len(opciones)):
            opcion_x = root[i][1][j].text.strip()
            puntuacion_de_pregunta = root[i][1][j].get("valor")
            tuplas_opciones.append((opcion_x, float(puntuacion_de_pregunta)))

        pregunta_usuario = Question(nombre, enunciado, tuplas_opciones, int(puntos))
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

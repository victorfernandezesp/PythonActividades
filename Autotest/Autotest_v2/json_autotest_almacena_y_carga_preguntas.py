"""
        Ejercicio Autotest V1.2:

            Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
            Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import json
import sys

from Autotest.Autotest_v1.pt2.question import Question

def guarda_preguntas():
    nombre_de_fichero = sys.argv[1]
    with open(nombre_de_fichero, encoding='utf-8') as archivo_a_escribir:
        while True:
            titulo_pregunta = input("Introduce el título de la pregunta:    ")
            enunciado_pregunta = input("Introduce el enunciado de la pregunta:  ")
            for opcion in range(4):
                opcion_de_pregunta = input("Introduce una opción de la pregunta:    ")
                while True:
                    valor_de_pregunta = input("Introduce el valor de la opción de la pregunta:    ")
                    try:
                        comprueba_valor_de_pregunta_es_float = float(valor_de_pregunta)
                    except:
                        print("Introduce un número real")
                        continue
                    break
            # TODO escribir el python, tengo dudas sobre como escribir las opciones ademas da IO error
            json.dump(ensure_ascii=False, indent=4)
            pregunta_usuario_si_sigue = input("Si no quieres introducir mas preguntas introduce un (N):     ")
            if pregunta_usuario_si_sigue.upper() == "N":
                break



def main():
    nombre_de_fichero = sys.argv[1]
    with open(nombre_de_fichero, encoding='utf-8') as cadena_de_preguntas:
        archivo_sacar_preguntas = json.load(cadena_de_preguntas)
    for i in range(len(archivo_sacar_preguntas)):
        titulo = archivo_sacar_preguntas[i]["titulo"]
        enunciado = archivo_sacar_preguntas[i]["enunciado"]

        opcion1 = archivo_sacar_preguntas[i]["opciones"][0]["opcion"]
        valor_opcion1 = archivo_sacar_preguntas[i]["opciones"][0]["valor"]

        opcion2 = archivo_sacar_preguntas[i]["opciones"][1]["opcion"]
        valor_opcion2 = archivo_sacar_preguntas[i]["opciones"][1]["valor"]

        opcion3 = archivo_sacar_preguntas[i]["opciones"][2]["opcion"]
        valor_opcion3 = archivo_sacar_preguntas[i]["opciones"][2]["valor"]

        opcion4 = archivo_sacar_preguntas[i]["opciones"][3]["opcion"]
        valor_opcion4 = archivo_sacar_preguntas[i]["opciones"][3]["valor"]

        opciones = ([(opcion1, float(valor_opcion1)), (opcion2, float(valor_opcion2)), (opcion3, float(valor_opcion3)), (opcion4, float(valor_opcion4))])
        pregunta_usuario = Question(titulo, enunciado, opciones, 1)
        pregunta_usuario.muestra_pregunta()
        pregunta_usuario.respuesta_usuario()


if __name__ == '__main__':
    main()

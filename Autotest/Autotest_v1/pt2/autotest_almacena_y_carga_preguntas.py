"""
        Ejercicio Autotest V1.2:

            Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
            Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

from Autotest.Autotest_v1.pt2.question import Question

def guarda_preguntas():
    nombre_de_fichero = sys.argv[1]
    with open(nombre_de_fichero, 'w', encoding='utf-8') as archivo_a_escribir:
        while True:
            titulo_pregunta = input("Introduce el título de la pregunta:    ")
            archivo_a_escribir.write(titulo_pregunta + "\n")
            enunciado_pregunta = input("Introduce el enunciado de la pregunta:  ")
            archivo_a_escribir.write(enunciado_pregunta + "\n")
            archivo_a_escribir.write("." + "\n")
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
                archivo_a_escribir.write(opcion_de_pregunta + "\n")
                archivo_a_escribir.write(valor_de_pregunta + "\n")
            archivo_a_escribir.write("---" + "\n")
            pregunta_usuario_si_sigue = input("Si no quieres introducir mas preguntas introduce un (N):     ")
            if pregunta_usuario_si_sigue.upper() == "N":
                break



def main():
    nombre_de_fichero = sys.argv[1]
    with open(nombre_de_fichero, 'r', encoding='utf-8') as cadena_de_preguntas:
        archivo_sacar_preguntas = cadena_de_preguntas.read()
    delimitador = "---"
    num_preguntas = archivo_sacar_preguntas.count(delimitador)

    with open(nombre_de_fichero, 'r', encoding='utf-8') as preguntas:
        archivo = preguntas.readlines()

    archivo = [line.strip() for line in archivo]

    contador_pregunta = 0
    while contador_pregunta < num_preguntas:
        lista_pregunta = []
        for j in archivo:
            if j == delimitador:
                break
            lista_pregunta.append(j)
        nombre = lista_pregunta.pop(0)
        enunciado = ""
        num_registros_a_eliminar = 0
        for i in range(len(lista_pregunta)):
            if lista_pregunta[i] == ".":
                num_registros_a_eliminar = i+1
                break
            enunciado += lista_pregunta[i]
        for k in range(num_registros_a_eliminar):
            lista_pregunta.remove(lista_pregunta[0])

        opciones = ([(lista_pregunta[0], float(lista_pregunta[1])), (lista_pregunta[2], float(lista_pregunta[3])), (lista_pregunta[4], float(lista_pregunta[5])), (lista_pregunta[6], float(lista_pregunta[7]))])
        pregunta_usuario = Question(nombre, enunciado, opciones, 1)
        pregunta_usuario.muestra_pregunta()
        pregunta_usuario.respuesta_usuario()
        contador_pregunta += 1
        elimina_hasta = 0
        for l in range(len(archivo)):
            if archivo[l] == delimitador:
                elimina_hasta = l + 1
                break
        for k in range(elimina_hasta):
            archivo.remove(archivo[0])

if __name__ == '__main__':
    main()

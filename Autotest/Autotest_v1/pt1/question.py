"""
        Ejercicio Autotest V1:

            Se pretende crear una aplicación que haga exámenes tipo test similares a como los realiza la
            plataforma Moodle con una sola respuesta. Esta plataforma permite crear un cuestionario, añadirle
            preguntas, ejecutarlo y dar una calificación

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from time import sleep

from typeguard import typechecked


class Respuesta_No_Encontrada(ValueError):
    def __init__(self):
        super().__init__(f"La respuesta introducida no coincide con ninguna de las posibles elecciones.")


@typechecked
class Question:
    __contador_preguntas = 0

    def __init__(self, nombre: str, enunciado: str, elecciones: list[tuple[str, float]], puntuacion: float = 1):
        self.__nombre = nombre
        self.__enunciado = enunciado
        self.__elecciones = elecciones
        self.__puntuacion = puntuacion
        Question.__contador_preguntas += 1

    @property
    def nombre(self):
        return self.__nombre

    @property
    def enunciado(self):
        return self.__enunciado

    @property
    def elecciones(self):
        return self.__elecciones

    @property
    def puntuacion(self):
        return self.__puntuacion

    @property
    def puntuacion_obtenida(self):
        return self.__puntuacion_obtenida

    def muestra_pregunta(self):
        print(f"------------------------------------------------")
        print(f"Pregunta {Question.__contador_preguntas}:")
        print(f"{self.__enunciado}")
        print(f"------------------------------------------------")
        print(f"Opciones:")
        print(f"------------------------------------------------")
        for eleccion in self.__elecciones:
            print(f"* {eleccion[0]}")

    def respuesta_usuario(self):
        respuesta = input("¿Cuál es la respuesta correcta?:     ")
        elecciones_de_pregunta = []
        for i in self.__elecciones:
            elecciones_de_pregunta.append(i[0])
        if respuesta not in elecciones_de_pregunta and respuesta != "":
            raise Respuesta_No_Encontrada()
        elif respuesta == "":
            puntuacion_obtenida = 0
            self.imprimir_puntuacion_obtenida(puntuacion_obtenida)
        else:
            puntuacion_obtenida = self.averigua_puntuacion_sacada_de_la_pregunta(elecciones_de_pregunta, respuesta)
            self.imprimir_puntuacion_obtenida(puntuacion_obtenida)

    @staticmethod
    def imprimir_puntuacion_obtenida(puntuacion_obtenida):
        sleep(1.25)
        print(f"Puntuación obtenida: {puntuacion_obtenida}")
        sleep(1.25)

    def averigua_puntuacion_sacada_de_la_pregunta(self, elecciones_de_pregunta, respuesta):
        posicion_de_la_respuesta_correcta = 0
        for j in range(len(elecciones_de_pregunta)):
            if elecciones_de_pregunta[j] == respuesta:
                posicion_de_la_respuesta_correcta = j
        valor_de_eleccion = []
        for i in self.__elecciones:
            valor_de_eleccion.append(i[1])
        return self.__puntuacion * valor_de_eleccion[posicion_de_la_respuesta_correcta]


if __name__ == '__main__':
    pr1 = Question("Planta vs Agua", "En relación con los tipos Pokemon, ¿Qué relación tiene el tipo Planta Vs Agua?",
                   ([("Muy efectivo", 1), ("Efectivo", -0.25), ("Poco efectivo", -0.50), ("No afecta", -0.75)]), 1)
    pr1.muestra_pregunta()
    pr1.respuesta_usuario()

    pr2 = Question("Normal vs Normal",
                   "En relación con los tipos Pokemon, ¿Qué relación tiene el tipo Normal Vs Normal?",
                   ([("Muy efectivo", -0.25), ("Efectivo", 1), ("Poco efectivo", -0.25), ("No afecta", -0.50)]), 1)
    pr2.muestra_pregunta()
    pr2.respuesta_usuario()

    pr3 = Question("Dragon vs Hada",
                   "En relación con los tipos Pokemon, ¿Qué relación tiene el tipo Dragon Vs Hada?",
                   ([("Muy efectivo", -0.75), ("Efectivo", -0.25), ("Poco efectivo", 1), ("No afecta", -0.25)]), 1)
    pr3.muestra_pregunta()
    pr3.respuesta_usuario()

    pr4 = Question("Normal vs Fantasma",
                   "En relación con los tipos Pokemon, ¿Qué relación tiene el tipo Normal vs Fantasma?",
                   ([("Muy efectivo", -0.75), ("Efectivo", -0.50), ("Poco efectivo", -0.25), ("No afecta", 1)]), 1)
    pr4.muestra_pregunta()
    pr4.respuesta_usuario()

    pr5 = Question("Dragon vs Dragon",
                   "En relación con los tipos Pokemon, ¿Qué relación tiene el tipo Dragon vs Dragon?",
                   ([("Muy efectivo", 1), ("Efectivo", -0.25), ("Poco efectivo", -0.75), ("No afecta", -0.50)]), 1)
    pr5.muestra_pregunta()
    pr5.respuesta_usuario()

"""
    Ejercicio 11:
        Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar
        unos a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del
        programa principal que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono
        tienen que validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve
        dígitos) y no puede haber dos terminales con el mismo número.

        Programa principal:

        t1 = Terminal("678112233")
        t2 = Terminal("644744469")
        t3 = Terminal("622328909")
        t4 = Terminal("664739818")
        print(t1)
        print(t2)
        t1.call(t2, 320)
        t1.call(t3, 200)
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        Salida:

        No 678 11 22 33 - 0 s de conversación
        No 644 74 44 69 - 0 s de conversación
        No 678 11 22 33 - 520 s de conversación
        No 644 74 44 69 - 320 s de conversación
        No 622 32 89 09 - 200 s de conversación
        No 664 73 98 18 - 0 s de conversación


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked

LONGITUD_NUMERO = 9


@typechecked
class Terminal:
    __listado_terminales = []

    @classmethod
    def listado_terminales(cls):
        return cls.__listado_terminales

    def __init__(self, numero: str):
        self.comprueba_numero(numero)
        Terminal.__listado_terminales.append(numero)
        self.__numero = numero
        self.__segundos_de_conversacion = 0

    @staticmethod
    def comprueba_numero(numero):
        if len(numero) != LONGITUD_NUMERO or not numero.isdigit():
            raise ValueError(f"El número debe tener una longitud de {LONGITUD_NUMERO} dígitos.")
        if numero[0] not in ["6", "7", "9"]:
            raise ValueError("El número debe empezar por 6, 7 o 9.")
        if numero in Terminal.__listado_terminales:
            raise ValueError("El número ya esta registrado.")

    @property
    def numero(self):
        return self.__numero[:3] + " " + self.__numero[3:5] + " " + self.__numero[5:7] + " " + self.__numero[7:9]

    @property
    def segundos_de_conversacion(self):
        return self.__segundos_de_conversacion

    def llama(self, other, segundos):
        if segundos < 0:
            raise ValueError("No puedes hacer llamadas de segundos negativos.")

        if self.__numero == other.__numero:
            raise ValueError("No puedes llamarte a ti mismo.")

        self.__segundos_de_conversacion += segundos
        other.__segundos_de_conversacion += segundos

    def __repr__(self):
        return f"Nº {self.numero} - {self.__segundos_de_conversacion}s de conversación "

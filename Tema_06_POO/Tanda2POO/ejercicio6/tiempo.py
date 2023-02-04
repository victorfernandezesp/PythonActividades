"""
    Ejercicio 6:
        Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de
        tiempo y se crean de la forma:

        t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

        t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

        t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

        Crea los getters y setters mediante propiedades y métodos para:

        -   Sumar y restar objetos de la clase (el resultado es otro objeto).
        -   Sumar y restar segundos, minutos y/u horas (se cambia el objeto actual).
        -   Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea
            10 h 35 m 5 s.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, horas: int = 0, minutos: int = 0, segundos: int = 0):
        self.horas = horas + (minutos // 60)
        self.minutos = (minutos % 60) + (segundos // 60)
        self.segundos = segundos % 60

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, value: int):
        self.__horas = value

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value: int):
        self.__minutos = value

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value: int):
        self.__segundos = value

    def __str__(self):
        return f"{self.__horas}H {self.__minutos}M {self.__segundos}S "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__horas}H {self.__minutos}M {self.__segundos}S )"

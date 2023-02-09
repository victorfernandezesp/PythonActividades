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
    def __init__(self, horas, minutos=None, segundos=None):
        if isinstance(horas, Duration):
            other = horas
            self.__horas = other.horas
            self.__minutos = other.minutos
            self.__segundos = other.segundos

        else:
            self.__horas = horas
            self.__minutos = minutos
            self.__segundos = segundos
            self.__normalizar()

    def __normalizar(self):
        segundos = self.horas * 3600 + self.minutos * 60 + self.segundos
        if segundos < 0:
            raise ValueError("El tiempo no puede ser negativo")

        self.__horas = segundos // 3600
        self.__minutos = segundos % 3600 // 60
        self.__segundos = segundos % 3600 % 60

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, value: int):
        nuevo_duration = Duration(value, self.minutos, self.segundos)
        self.__horas = nuevo_duration.horas
        self.__minutos = nuevo_duration.minutos
        self.__segundos = nuevo_duration.segundos

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value: int):
        nuevo_duration = Duration(self.horas, value, self.segundos)
        self.__horas = nuevo_duration.horas
        self.__minutos = nuevo_duration.minutos
        self.__segundos = nuevo_duration.segundos

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value: int):
        nuevo_duration = Duration(self.horas, self.minutos, value)
        self.__horas = nuevo_duration.horas
        self.__minutos = nuevo_duration.minutos
        self.__segundos = nuevo_duration.segundos

    def __add__(self, other):
        return Duration(self.horas + other.horas, self.minutos + other.minutos, self.segundos + other.segundos)

    def __sub__(self, other):
        return Duration(self.horas - other.horas, self.minutos - other.minutos, self.segundos - other.segundos)

    def sumar_horas(self, horas):
        self.__horas += horas

    def sumar_minutos(self, minutos):
        self.__minutos += minutos

    def sumar_segundos(self, segundos):
        self.__segundos += segundos

    def restar_horas(self, horas):
        self.__horas -= horas

    def restar_minutos(self, minutos):
        self.__minutos -= minutos

    def restar_segundos(self, segundos):
        self.__segundos -= segundos

    def __str__(self):
        return f"{self.__horas}H {self.__minutos}M {self.__segundos}S "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__horas}H {self.__minutos}M {self.__segundos}S )"

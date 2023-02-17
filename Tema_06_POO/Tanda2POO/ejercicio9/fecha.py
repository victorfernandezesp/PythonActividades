"""
    Ejercicio 9:
       Nos hemos enterado de que la clase datetime. Date ha sido comprometida y tenemos que crear una clase nueva para
       almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o
       año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

        f1 = Date(1, 10, 2020)  # almacena el 1 de octubre de 2020
        f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

        Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

        Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

        Crea métodos para:

        - Sumar y restar días a la fecha.

        - Restar fechas. Devuelve el número de días comprendidos entre ambas.

        - Comparar la fecha almacenada con otra.

        - Saber si el año de la fecha almacenada es bisiesto.

        - Obtener el día de la semana de una fecha concreta.

        - El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


class Fecha:
    def __init__(self, dia:int, mes, ano):
        if isinstance(dia, Fecha):
            if mes is not None or ano is not None:
                raise TypeError("Un objeto creado por otro objeto, no puedes pasarle mas de un parámetro")
            other = dia
            self.dia = other.dia
            self.mes = other.mes
            self.ano = other.ano
        else:
            self.dia = dia
            self.mes = mes
            self.ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        self.__mes = value

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, value):
        self.__ano = value

    def __str__(self):
        return f"{self.dia}, {self.mes}, {self.ano} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.dia}, {self.mes}, {self.ano}  )"

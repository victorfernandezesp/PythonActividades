"""
    Ejercicio 2:
        Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y
        setters (propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además, la clase
        debe tener un __str__() para poder imprimir los puntos en formato “(x, y)”. Implementa un test donde crees un
        punto, lo imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su
        coordenada x, y vuelvas a imprimir el punto.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


class Point:
    def __init__(self):
        self.coo_x = 0
        self.coo_y = 0

    @property
    def coo_x(self):
        return self.__coo_x

    @property
    def coo_y(self):
        return self.__coo_y

    def invert_coordinates(self, x, y):
        punto_auxiliar = x
        x = y
        y = punto_auxiliar

        self.__coo_x = x
        self.__coo_y = y

    @coo_x.setter
    def coo_x(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{value} no es un objeto de tipo entero.")
        self.__coo_x = value

    @coo_y.setter
    def coo_y(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{value} no es un objeto de tipo entero.")
        self.__coo_y = value

    def __str__(self):
        return f"Los puntos invertidos es igual a: ({self.__coo_x}, {self.__coo_y})"

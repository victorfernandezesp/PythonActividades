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
from typeguard import typechecked


class Point:
    @typechecked
    def __init__(self, coo_x: int = 0, coo_y: int = 0):
        self.coo_x = coo_x
        self.coo_y = coo_y

    @property
    def coo_x(self):
        return self.__coo_x

    @property
    def coo_y(self):
        return self.__coo_y

    @coo_x.setter
    @typechecked
    def coo_x(self, value: int):
        self.__coo_x = value

    @coo_y.setter
    @typechecked
    def coo_y(self, value: int):
        self.__coo_y = value

    def invert_coordinates(self):
        self.__coo_x, self.__coo_y = self.__coo_y, self.__coo_x

    def __str__(self):
        return f"({self.__coo_x}, {self.__coo_y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__coo_x}, {self.__coo_y})"

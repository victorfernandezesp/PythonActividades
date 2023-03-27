"""
        Ejercicio 7:

            Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la
            compra. Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista,
            por tanto, deberás crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del
            producto, su precio y la cantidad (número de unidades de dicho producto). A continuación se muestra tanto el
            contenido del programa principal como la salida que debe mostrar el programa. Los métodos a implementar se
            pueden deducir del programa principal.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


class Elemento:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = self.precio * self.cantidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value: float):
        self.__precio = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value: int):
        self.__cantidad = value

    @property
    def subtotal(self):
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value: float):
        self.__subtotal = value
    def __repr__(self):
        return f"{self.__nombre}, {self.__precio} {self.__cantidad}"

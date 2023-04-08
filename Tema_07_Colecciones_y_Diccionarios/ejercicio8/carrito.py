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
from Tema_07_Colecciones_y_Diccionarios.ejercicio7.elemento import Elemento


class Carrito:

    def __init__(self):
        self.__contenido = []
        self.__objetos_del_carrito = 0
        self.__coste_del_carrito = 0

    @property
    def contenido(self):
        return self.__contenido

    @property
    def objetos_del_carrito(self):
        return self.__objetos_del_carrito

    @property
    def coste_del_carrito(self):
        return self.__coste_del_carrito

    def agrega(self, elemento: Elemento):
        for i in range(len(self.__contenido)):
            elemento_de_lista = self.__contenido[i]
            if elemento_de_lista.nombre == elemento.nombre:
                elemento_de_lista.cantidad += 1
                elemento_de_lista.subtotal += elemento.precio
        # TODO aunque las cuentas estan bien me refleja el producto repetido pese a que su cantidad y su total no se
        #  sume
        if elemento not in self.__contenido:
            self.__objetos_del_carrito += elemento.cantidad
            self.__coste_del_carrito += elemento.subtotal
            self.__contenido.append(elemento)

    def numero_elementos(self):
        return self.__objetos_del_carrito

    def importe_total(self):
        return self.__coste_del_carrito

    def muestra_contenido(self):
        for i in self.__contenido:
            elemento: Elemento = i
            print(f"Articulo: {elemento.nombre}, Coste:{elemento.precio}, Cantidad: {elemento.cantidad}, "
                  f"Subtotal: {round(elemento.subtotal, 4)}")
        return ""

    def __repr__(self):
        return self.muestra_contenido()

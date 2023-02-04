"""
    Ejercicio 5:
        Crea una clase que represente una estructura de datos tipo pila (stack) y otro tipo cola (queue).

        La pila y la cola permitirán estas operaciones:

        *   Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
        *   Obtener el número de elementos almacenados (tamaño).
        *   Saber si la pila o la cola está vacía.
        *   Vaciar completamente la pila o la cola.

        Para el caso de la pila:
        -   Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
        -   Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
        -   Leer el elemento superior de la pila sin retirarlo (top).

        -
        Para el caso de la cola:
        -   Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
        -   Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir,
                                    el primer elemento que entró.
        -   Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


@typechecked
class Cola:
    def __init__(self, *valores):
        if len(valores) == 1 and isinstance(valores[0], Cola):
            list(valores)
            self.valores = valores[0]
        else:
            self.valores = list(valores)

    @property
    def valores(self):
        return self.__valores.copy()

    @valores.setter
    def valores(self, value):
        self.__valores = value

    def obtener_numero_elementos(self):
        return len(self.__valores)

    def esta_vacia(self):
        if not self.__valores:
            return "Esta vacia"
        return "Tiene contenido"

    def vaciar_cola(self):
        self.__valores.clear()

    def encolar(self, elemento):
        self.__valores.append(elemento)

    def descolar(self):
        return self.__valores.pop(0)

    def leer_frontal_cola(self):
        return self.__valores[0]

    def __str__(self):
        return f"({self.__valores})"

    def __repr__(self):
        return f"{self.__valores}"

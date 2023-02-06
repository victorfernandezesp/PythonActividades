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
from Tema_06_POO.Tanda2POO.ejercicio5.pila import Pila

print("----------------------------")
print("PILA 1:  ")
print("----------------------------")
pila1 = Pila(1, 2, 3, 4, 5)
print(f"La pila1 = {pila1}")
print(f"La longitud de la pila es: {pila1.obtener_numero_elementos()}")
print(f"{pila1.esta_vacia()}")
pila1.apilar(1)
print(f"La pila, apilada: {pila1}")
print(f"El elemento que se ha desapilado: {pila1.desapilar(2)}.  ")
print(f"La pila después de desapilar: {pila1}")
print(f"El elemento top de la pila: {pila1.leer_top_pila()}")
pila1.vaciar_pila()
print(f"La pila vacia: {pila1}")

print("----------------------------")

print("PILA 2:  ")
print("----------------------------")
pila2 = Pila()
print(f"La pila2 = {pila2}")
print(f"La longitud de la pila es: {pila2.obtener_numero_elementos()}")
pila2.apilar(1)
pila2.apilar(2)
pila2.apilar(3)
pila2.apilar(4)
print(f"La pila, apilada: {pila2}")
print(f"El elemento que se ha desapilado: {pila2.desapilar(0)}.  ")
print(f"La pila después de desapilar: {pila2}")
print(f"El elemento top de la pila: {pila2.leer_top_pila()}")
pila2.vaciar_pila()
print(f"La pila vacia: {pila2}")

print("----------------------------")
print("PILA 3:  ")
print("----------------------------")
pila1 = Pila(1, 2, 3)
pila3 = Pila(pila1)
print(f"La pila3 = {pila3}")
print(f"La longitud de la pila es: {pila3.obtener_numero_elementos()}")
pila3.apilar(1)
pila3.apilar(2)
pila3.apilar(3)
pila3.apilar(4)
print(f"La pila, apilada: {pila3}")
print(f"El elemento que se ha desapilado: {pila3.desapilar(0)}.  ")
print(f"La pila después de desapilar: {pila3}")
print(f"El elemento top de la pila: {pila3.leer_top_pila()}")
pila3.vaciar_pila()
print(f"La pila vacia: {pila3}")

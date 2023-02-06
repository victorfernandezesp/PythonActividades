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

from Tema_06_POO.Tanda2POO.ejercicio5.cola import Cola

print("----------------------------")
print("COLA 1:  ")
print("----------------------------")
cola1 = Cola(1, 2, 3, 4, 5)
print(f"La cola1 = {cola1}")
print(f"La longitud de la cola es: {cola1.obtener_numero_elementos()}")
print(f"{cola1.esta_vacia()}")
cola1.encolar(1)
print(f"La cola encolada: {cola1}")
print(f"El elemento que se ha descolado: {cola1.descolar()}.  ")
print(f"La cola después de desencolar: {cola1}")
print(f"El elemento frontal de la cola: {cola1.leer_frontal_cola()}")
cola1.vaciar_cola()
print(f"La cola vacia: {cola1}")

print("----------------------------")

print("COLA 2:  ")
print("----------------------------")
cola2 = Cola()
print(f"La cola2 = {cola2}")
print(f"La longitud de la cola es: {cola2.obtener_numero_elementos()}")
print(f"{cola2.esta_vacia()}")
cola2.encolar(1)
cola2.encolar(2)
cola2.encolar(3)
print(f"La cola encolada: {cola2}")
print(f"El elemento que se ha descolado: {cola2.descolar()}.  ")
print(f"La cola después de desencolar: {cola2}")
print(f"El elemento frontal de la cola: {cola2.leer_frontal_cola()}")
cola2.vaciar_cola()
print(f"La cola vacia: {cola2}")


cola1 = Cola(1, 2, 3)
print("COLA 3:  ")
print("----------------------------")
cola3 = Cola(cola1)
print(f"La cola3 = {cola3}")
print(f"La longitud de la cola es: {cola3.obtener_numero_elementos()}")
print(f"{cola3.esta_vacia()}")
cola3.encolar(1)
print(f"La cola encolada: {cola3}")
print(f"El elemento que se ha descolado: {cola3.descolar()}.  ")
print(f"La cola después de desencolar: {cola3}")
print(f"El elemento frontal de la cola: {cola3.leer_frontal_cola()}")
cola3.vaciar_cola()
print(f"La cola vacia: {cola3}")

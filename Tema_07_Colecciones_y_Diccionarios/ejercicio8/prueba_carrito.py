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
from Tema_07_Colecciones_y_Diccionarios.ejercicio8.carrito import Carrito
from Tema_07_Colecciones_y_Diccionarios.ejercicio8.elemento import Elemento

mi_carrito = Carrito()
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")

print("\nContinúa la compra...\n")
mi_carrito.agrega(Elemento("Samsung Galaxy Tab", 199, 3))
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
print(mi_carrito)
print(f"Ahora hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")

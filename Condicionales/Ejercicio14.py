""" Ejercicio 14.
        La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica
        en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y
        tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando
        lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos
        si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de
        tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import sys

PRECIO_B2 = 0.50

PRECIO_B1 = 0.30

PRECIO_A2 = 0.30

PRECIO_A1 = 0.20

TIPO_ERROR_TAMANHO = 2

TIPO_ERROR_UVA = 1

print("Este programa te calcula el precio de la uva según su tipo y tamaño  ")
num_kilos = int(input("Introduce el numero de kilos, por favor! "))

tipo = input("Introduce el tipo de uva (A o B), por favor! ")
tipo = tipo.upper()
if tipo not in "AB":
    print(f"ERROR.Escoja una tipo de tamaño arriba mencionado", file=sys.stderr)
    sys.exit(TIPO_ERROR_UVA)

tamanho = input("Introduce el tamaño de la uva (1 o 2), por favor! ")
if tamanho not in "12":
    print(f"ERROR.Escoja una tipo de  uva arriba mencionado", file=sys.stderr)
    sys.exit(TIPO_ERROR_TAMANHO)

precio_kilo = float(input("Escribe el precio del Kg de las uvas que se vende (Ejemplo: 1.20 ) "))

if tipo == "A" and tamanho == "1":
    precio_total = num_kilos * (precio_kilo + PRECIO_A1)
    print(f"El precio total de la uva con tamaño {tamanho} y tipo {tipo} sale a {round(precio_total,2)}€")

if tipo == "A" and tamanho == "2":
    precio_total = num_kilos * (precio_kilo + PRECIO_A2)
    print(f"El precio total de la uva con tamaño {tamanho} y tipo {tipo} sale a {round(precio_total,2)}€")

if tipo == "B" and tamanho == "1":
    precio_total = num_kilos * (precio_kilo + PRECIO_B1)
    print(f"El precio total de la uva con tamaño {tamanho} y tipo {tipo} sale a {round(precio_total,2)}€")

if tipo == "B" and tamanho == "2":
    precio_total = num_kilos * (precio_kilo + PRECIO_B2)
    print(f"El precio total de la uva con tamaño {tamanho} y tipo {tipo} sale a {round(precio_total,2)}€")

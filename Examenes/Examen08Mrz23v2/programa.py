"""
Programa de pruebas examen.
@author Victor Fernandez España
Curso 2022-2023
"""
import sys
from datetime import datetime

from Examenes.Examen08Mrz23.menu import Menu
from Examenes.Examen08Mrz23.cashregister import CashRegister
from Examenes.Examen08Mrz23.movement import Movement

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu1 = Menu("Caja Registradora",
             "Entrada de caja.",
             "Salida de caja.",
             "Borrado del último movimiento de la caja.",
             "Impresión de la caja.")

caja = CashRegister

while True:
    option = menu1.escoger()
    match option:

        case 1:
            """ Solo funciona ejecutándolo en consola """

            cantidad = float(input("Cantidad de la operación:   "))
            concepto = input("Concepto de la operación:   ")
            fecha_hora = datetime.now()
            caja.add(Movement(cantidad, concepto, fecha_hora))

        case 2:
            """ Solo funciona ejecutándolo en consola """

            cantidad = float(input("Cantidad de la operación:   "))
            concepto = input("Concepto de la operación:   ")
            fecha_hora = datetime.now()
            cantidad = cantidad * -1
            caja.add(Movement(cantidad, concepto, fecha_hora))

        case 3:
            CashRegister.delete_last()

        case 4:
            print(CashRegister)

        case _:
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)

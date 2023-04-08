"""
        Ejercicio 9:

            Amplía el ejercicio de la tanda anterior que implementaba cuentas corrientes de un banco de tal forma que
            cada cuenta lleve un registro de todos los movimientos realizados: ingresos, cargos y transferencias
            (tanto enviadas como recibidas).

            Contenido del programa principal:

            cuenta1 = CuentaCorriente()
            cuenta2 = CuentaCorriente(1500)
            cuenta3 = CuentaCorriente(6000)
            cuenta1.ingreso(2000)
            cuenta1.cargo(600)
            cuenta3.ingreso(75)
            cuenta1.cargo(55)
            cuenta2.transferencia(cuenta1, 100)
            cuenta1.transferencia(cuenta3, 250)
            cuenta3.transferencia(cuenta1, 22)
            print(cuenta1.movimientos())
            Salida:

            Movimientos de la cuenta 1654432813
            -----------------------------------
            Ingreso de 2000 € Saldo: 2000,00 €
            Cargo de 600 € Saldo: 1400,00 €
            Cargo de 55 € Saldo: 1345,00 €
            Transferencia recibida de 100 € de la cuenta 1654432813 Saldo 1445,00 €
            Transferencia emitida de 250 € a la cuenta 6546817008 Saldo 1195,00 €
            Transferencia recibida de 22 € de la cuenta 1654432813 Saldo 1217,00 €

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_07_Colecciones_y_Diccionarios.ejercicio9.banco import BankAccount


cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
cuenta1.ingresar(2000)
cuenta1.retirar(600)
cuenta3.ingresar(75)
cuenta1.retirar(55)
cuenta2.transferir(cuenta1, 100)
cuenta1.transferir(cuenta3, 250)
cuenta3.transferir(cuenta1, 22)
print(cuenta1.movimientos())
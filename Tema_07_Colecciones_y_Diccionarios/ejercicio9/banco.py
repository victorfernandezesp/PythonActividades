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
import random


class BankAccount:
    __listado_cuentas = []

    def __init__(self, saldo=0):
        posible_cuenta = self.__comprueba_cuenta(saldo)
        self.__numero_cuenta = posible_cuenta
        BankAccount.__listado_cuentas.append(posible_cuenta)
        self.__saldo = saldo
        self.__operacion_permitida = False
        self.__movimientos = []

    @staticmethod
    def __comprueba_cuenta(saldo):
        if saldo < 0:
            raise ValueError("No puedes crear una cuenta con saldo negativa")
        while True:
            posible_cuenta = random.randrange(1, 9999999999)
            if posible_cuenta not in BankAccount.__listado_cuentas:
                break
        return posible_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    def ingresar(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__saldo += cantidad
        self.__movimientos.append(f"Ingreso de {cantidad} € Saldo: {self.__saldo:.2f} €")

    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if 0 > (self.__saldo - cantidad):
            raise ValueError("No puedo realizar esta operación, su saldo seria inferior a 0")

        self.__saldo -= cantidad
        self.__operacion_permitida = True
        self.__movimientos.append(f"Retirada de {cantidad} € Saldo: {self.__saldo:.2f} €")

    def transferir(self, other, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if 0 > (self.__saldo - cantidad):
            raise ValueError("No puedo realizar esta operación, su saldo seria inferior a 0")

        self.__saldo -= cantidad
        self.__operacion_permitida = True
        if self.__operacion_permitida:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            other.__saldo += cantidad
        self.__movimientos.append(f"Transferencia emitida de {cantidad} € a la cuenta {other} ")
        self.__movimientos.append(f"Transferencia recibida de {cantidad} € de la cuenta {self.__numero_cuenta}, Saldo: {self.__saldo:.2f} €")

    def __repr__(self):
        return f"Número de cta: {self.__numero_cuenta:010d} Saldo: {float(self.__saldo)} €"

    def movimientos(self):
        print(f"Movimientos de {self.__numero_cuenta}")
        for i in range(len(self.__movimientos)):
            print(self.__movimientos[i])
        return ""

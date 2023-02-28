"""
        Ejercicio 13:

            Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de
            cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el
            mismo número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se
            pondrá a cero inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una
            transferencia entre una cuenta y otra. No se permite el saldo negativo.

            Programa principal:

            cuenta1 = BankAccount()
            cuenta2 = BankAccount(1500)
            cuenta3 = BankAccount(6000)
            print(cuenta1)
            print(cuenta2)
            print(cuenta3)
            cuenta1.deposit(2000)
            cuenta2.withdraw(600)
            cuenta3.deposit(75)
            cuenta1.withdraw(55)
            cuenta2.transfer(cuenta3, 100)
            print(cuenta1)
            print(cuenta2)
            print(cuenta3)
            Salida

            Número de cta: 6942541557 Saldo: 0,00 €
            Número de cta: 9319536518 Saldo: 1500,00 €
            Número de cta: 7396941518 Saldo: 6000,00 €
            Número de cta: 6942541557 Saldo: 1945,00 €
            Número de cta: 9319536518 Saldo: 800,00 €
            Número de cta: 7396941518 Saldo: 6175,00 €

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import random


class BankAccount:
    __listado_cuentas = []

    @classmethod
    def listado_cuentas(cls):
        return cls.__listado_cuentas

    def __init__(self, saldo=0):
        while True:
            posible_cuenta = random.randrange(1000000000, 9999999999)
            if posible_cuenta not in BankAccount.__listado_cuentas:
                break
        self.__numero_cuenta = posible_cuenta
        BankAccount.__listado_cuentas.append(posible_cuenta)
        self.__saldo = saldo
        self.__operacion_permitida = False

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    def ingresar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):

        if 0 > (self.__saldo - cantidad):
            print("No puedo realizar esta operación, su saldo seria inferior a 0")
        else:
            self.__saldo -= cantidad
            self.__operacion_permitida = True

    def transferir(self, other, cantidad):
        self.retirar(cantidad)
        if self.__operacion_permitida:
            other.__saldo += cantidad

    def __repr__(self):
        return f"{self.__class__.__name__} Número de cta: {self.__numero_cuenta} Saldo: {float(self.__saldo)} €"

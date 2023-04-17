"""
        Ejercicio 3:

            Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la
            clase un método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un
            fichero elegido por el cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior
            y cree el objeto con esos datos. Pruébalo con un programa.

            P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de
            error correspondiente.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import pickle
import random


class Saldo_Negativo_Error(TypeError):

    def __init__(self, saldo):
        super().__init__(f"El saldo tiene que ser positivo. Recibido: {saldo}")
        self.saldo = saldo


class Cantidad_Negativa_Error(TypeError):

    def __init__(self, cantidad):
        super().__init__(f"La cantidad no puede ser negativa. Recibido: {cantidad}")
        self.saldo = cantidad


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
            raise Saldo_Negativo_Error(saldo)
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
            raise Cantidad_Negativa_Error(cantidad)
        self.__saldo += cantidad
        self.__movimientos.append(f"Ingreso de {cantidad} € Saldo: {self.__saldo:.2f} €")

    def retirar(self, cantidad):
        if cantidad < 0:
            raise Cantidad_Negativa_Error(cantidad)
        if 0 > (self.__saldo - cantidad):
            raise Saldo_Negativo_Error(self.__saldo)

        self.__saldo -= cantidad
        self.__operacion_permitida = True
        self.__movimientos.append(f"Retirada de {cantidad} € Saldo: {self.__saldo:.2f} €")

    def transferir(self, other, cantidad):
        if cantidad < 0:
            raise Cantidad_Negativa_Error(cantidad)
        if 0 > (self.__saldo - cantidad):
            raise Saldo_Negativo_Error(self.__saldo)

        self.__saldo -= cantidad
        self.__operacion_permitida = True
        if self.__operacion_permitida:
            if cantidad < 0:
                raise Cantidad_Negativa_Error(cantidad)
            other.__saldo += cantidad
        self.__movimientos.append(f"Transferencia emitida de {cantidad} € a la cuenta {other} ")
        self.__movimientos.append(
            f"Transferencia recibida de {cantidad} € de la cuenta {self.__numero_cuenta}, Saldo: {self.__saldo:.2f} €")

    def __repr__(self):
        return f"Número de cta: {self.__numero_cuenta:010d} Saldo: {float(self.__saldo)} €"

    def movimientos(self):
        print(f"Movimientos de {self.__numero_cuenta}")
        for i in range(len(self.__movimientos)):
            print(self.__movimientos[i])
        return ""

    def convertir_objeto_a_archivo(self):
        nombre_fichero = str(self.__numero_cuenta) + '.pkl'
        with open(nombre_fichero, 'wb') as f:
            pickle.dump(self, f)


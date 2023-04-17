"""
        Ejercicio 2:

            Modifica el ejercicio de la cuenta corriente para que el método que almacena en un fichero el estado del
            objeto guarde el objeto entero y el que lo recupera lo restaure. En esta versión no le pasamos nombre de
            fichero al método a la hora de guardarlo, usará el número de cuenta corriente para ello.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_09_Ficheros.Tanda3.ejercicio1.banco import BankAccount


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
cuenta1.convertir_objeto_a_archivo()
cuenta2.convertir_objeto_a_archivo()
cuenta3.convertir_objeto_a_archivo()


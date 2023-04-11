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
from Tema_09_Ficheros.ejercicio3.banco import BankAccount


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

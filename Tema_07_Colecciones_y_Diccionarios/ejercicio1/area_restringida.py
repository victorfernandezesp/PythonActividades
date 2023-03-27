"""
        Ejercicio 1:

            Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y
            una contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área
            restringida”. El usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa
            dirá “Lo siento, no tiene acceso al área restringida”. Los nombres de usuario con sus correspondientes
            contraseñas deben estar almacenados en un diccionario.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
INTENTOS_MAXIMOS = 3


def main():
    CREDENCIALES = {"usuario": "usuario", "Andared": "llevalatararaunvestidoblancollenodecascabeles", "yo": "password"}
    intentos = 0
    while True:
        nombre_usuario = input("Introduce su nombre de usuario:     ")
        contrasenya = input("Introduce la contraseña:       ")
        if CREDENCIALES.get(nombre_usuario) is None or CREDENCIALES.get(nombre_usuario) != contrasenya:
            intentos += 1
            print("Las CREDENCIALES no son validas, introduzca de nuevo")
        else:
            print("Bienvenido al sistema")
            break

        if intentos == INTENTOS_MAXIMOS:
            print("Has agotado los intentos, vuelva mas tarde.")


if __name__ == "__main__":
    main()

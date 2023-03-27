"""
        Ejercicio 6:

            Realiza un programa que sepa decir la capital de un país (en caso de conocer la respuesta) y que, además,
            sea capaz de aprender nuevas capitales. En principio, el programa solo conoce las capitales de España,
            Portugal y Francia. Estos datos deberán estar almacenados en un diccionario. Los datos sobre capitales
            que vaya aprendiendo el programa se deben almacenar en el mismo diccionario. El usuario sale del programa
            escribiendo la palabra “salir”.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


def main():
    paises = {"España": "Madrid",
              "Portugal": "Lisboa",
              "Francia": "París"
              }
    while True:
        pais = input(f"Escribe el nombre de un país y te diré su capital:   ")
        if pais.lower() == "salir":
            break
        if paises.get(pais) is not None:
            print(f"La capital de {pais} es {paises.get(pais)}.")
        else:
            nueva_capital = input(f"No conozco la respuesta ¿Cuál es la capital de {pais}?:   ")
            if nueva_capital.lower() == "salir":
                break
            paises[pais] = nueva_capital
            print("Gracias por enseñarme nuevas capitales")


if __name__ == "__main__":
    main()

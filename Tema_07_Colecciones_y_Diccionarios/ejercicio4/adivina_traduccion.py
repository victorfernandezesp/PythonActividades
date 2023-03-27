"""
        Ejercicio 4:

            Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior.
            El programa irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y
            comprobará si son correctas. Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas
            erróneas.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import random

TEST_PALABRAS = 5


def main():
    PALABRAS_EN_DICCIONARIO = 20
    mini_diccionario = {"Hola": "Hello",
                        "Rojo": "Red",
                        "Azul": "Blue",
                        "Verde": "Green",
                        "Amarillo": "Yellow",
                        "Morado": "Purple",
                        "Blanco": "White",
                        "Negro": "Black",
                        "Móvil": "Mobile",
                        "Botella": "Bottle",
                        "Semana": "Week",
                        "Television": "TV",
                        "Pantalla": "Screen",
                        "Ordenador": "Computer",
                        "Portátil": "Laptop",
                        "Auriculares": "Headphones",
                        "Balón": "Ball",
                        "Gafas": "Glasses",
                        "Plato": "Dish",
                        "Cuchara": "Spoon"
                        }
    total_lista = list(mini_diccionario.items())
    palabras_escogidas = []
    for i in range(TEST_PALABRAS):
        num_random = random.randrange(PALABRAS_EN_DICCIONARIO)
        palabra = total_lista.pop(num_random)
        PALABRAS_EN_DICCIONARIO -= 1
        palabras_escogidas.append(palabra)

    palabras_escogidas = dict(palabras_escogidas)
    bien = 0
    mal = 0

    for j in palabras_escogidas.keys():
        palabra = input(f"Cual es la traducción de la palabra {j}:  ")
        if mini_diccionario.get(j) != palabra:
            mal += 1
        else:
            bien += 1
    print(f"Has tenido {bien} BIEN y {mal} MAL. ")


if __name__ == "__main__":
    main()

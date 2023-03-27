"""
        Ejercicio 3:

            Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente
            traducción). Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra
            en español y dará la correspondiente traducción en inglés.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


def main():
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
                        "Cuchara": "Spoon"}

    while True:
        palabra_usuario = input("Introduce su palabra en español:     ")
        if palabra_usuario == "":
            break
        if mini_diccionario.get(palabra_usuario) is None:
            print(f"La palabra {palabra_usuario} no se encuentra en nuestro diccionario, disculpe las molestias .")
        else:
            print(f"La palabra {palabra_usuario} traducida al ingles es {mini_diccionario.get(palabra_usuario)}.")


if __name__ == "__main__":
    main()

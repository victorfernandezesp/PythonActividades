"""
    Ejercicio 4:
        Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formas de construir un dado (uno
        al que no se le pasa nada e inicializa el dado al azar, otro al que solo se le pasa que número tiene el dado en
        la cara superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa
        los getters, el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un
        vector de 4 dados y los lance una serie de veces.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from time import sleep
from dado import Dado

VECES_QUE_SE_LANZAN = 3

dado0 = Dado()
dado1 = Dado()
dado2 = Dado(3)
dado3 = Dado(8, 12)

vector_4_dados = [dado0, dado1, dado2, dado3]

for i in range(VECES_QUE_SE_LANZAN):
    print(f"_______TIRADA {i + 1}_______")
    for j in range(len(vector_4_dados)):
        vector_4_dados[j].roll()
        print(f"Ha salido: {vector_4_dados[j]}")
    sleep(1.5)

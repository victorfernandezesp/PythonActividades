""" Ejercicio 16.
       La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que
       ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80
       céntimos por minuto, los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50
       céntimos por minuto.

        Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de
        tarde, 10%. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una
        llamada.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

NI_MANHANA_NI_TARDE_ERROR = 3

NI_SI_NI_NO_ERROR = 2

TIEMPO_MIN_LLAMADA_ERROR = 1

print("Este programa calcula el costo de una llamada con precio progresivo")
tiempo = int(input("¿Cuántos minutos ha durado la llamada?: "))

if tiempo <= 0:
    print(f"ERROR. El tiempo minimo de una llamada es de 1 minuto", file=sys.stderr)
    sys.exit(TIEMPO_MIN_LLAMADA_ERROR)

domingo = input("Has realizado la llamada el Domingo? (S/N): ")
if domingo not in "SN":
    print(f"ERROR. Tienes que elaborar una respuesta afirmativa o negativa ", file=sys.stderr)
    sys.exit(NI_SI_NI_NO_ERROR)

coste = 0

if domingo == "N":
    if tiempo <= 5:
        coste = tiempo * 1
    elif tiempo <= 8:
        coste = (tiempo - 5) * 80 + 500
    elif tiempo <= 10:
        coste = (tiempo - 8) * 70 + 240 + 500
    else:
        coste = (tiempo - 10) * 50 + 140 + 240 + 500

    turno = input("¿Qué turno, mañana o tarde? (M/T)?: ")
    if turno not in "MT":
        print(f"ERROR. Tienes que elaborar una respuesta mañana o tarde ", file=sys.stderr)
        sys.exit(NI_MANHANA_NI_TARDE_ERROR)
    if turno == "M":
        coste = coste * 1.15
    else:
        coste = coste * 1.10

if domingo == "S":

    coste = coste * 1.03

print(f"El coste de la llamada: {coste} €.")

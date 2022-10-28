""" Ejercicio 20.
        Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central,
         América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona
          a la que va dirigido. Lo anterior se muestra en la tabla:

        ZONA	UBICACIÓN	COSTO/GRAMO
        1	América del Norte	24.00 euros
        2	América Central	20.00 euros
        3	América del Sur	21.00 euros
        4	Europa	10.00 euros
        5	Asia	18.00 euros
        Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por
        cuestiones de logística y de seguridad.
        Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la
        entrega.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

CARGAMENTO_INSUFICIENTE_ERROR = 1
print("Este programa te dice los dias del mes introduciendo el numero de mes ")
kilo = float(input("Dígame cuantos gramos pesa el pedido(En gramos), por favor! "))

if kilo < 5000:
    print(f"ERROR. Tiene que hacer un pedido maximo de 5000 gramos ", file=sys.stderr)
    sys.exit(CARGAMENTO_INSUFICIENTE_ERROR)
else:
    zona = int(input("Dígame la zona donde se va a enviar: "))
    print("1-AM.NOR.")
    print("2-AM.CEN.")
    print("3-AM.SUR.")
    print("4-EU. ")
    print("5-AS. ")
    match zona:
        case 1:
            print("El coste del envío seria de:", 24.00 * kilo, "€")
        case 2:
            print("El coste del envío seria de:", 20.00 * kilo, "€")
        case 3:
            print("El coste del envío seria de:", 21.00 * kilo, "€")
        case 4:
            print("El coste del envío seria de:", 10.00 * kilo, "€")
        case 5:
            print("El coste del envío seria de:", 18.00 * kilo, "€")

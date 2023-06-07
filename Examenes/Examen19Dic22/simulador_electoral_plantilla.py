"""
Examen 19-Dic-2022:
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.

Autor: Víctor Fernández España
Curso:2022/2023
"""
from utilities import menu

PORCENTAJE_MINIMO_VOTOS = 0.05

ciudad = None
votos_validos = 0
concejales = 0
partidos_con_votos = []
partidos = []
votos = []


def main():
    introducir_o_cargar_datos = False
    while True:
        opcion = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if opcion == 1:
            cargar_datos_electorales_de_cordoba()
            introducir_o_cargar_datos = True
        elif opcion == 2:
            introducir_datos_electorales()
            introducir_o_cargar_datos = True
        elif opcion == 3:
            if introducir_o_cargar_datos:
                introducir_partidos_y_votos()
            else:
                print("ERROR. Primero tienes que introducir los datos, elija la opcion 1 o 2 antes de ejecutar esta. ")
        elif opcion == 4:
            if introducir_o_cargar_datos:
                calcular_e_imprimir_simulacion()
            else:
                print("ERROR. Primero tienes que introducir los datos, elija la opcion 1 o 2 antes de ejecutar esta. ")
        else:
            break
        print()

    print("¡Hasta la próxima! ;-)")


def cargar_datos_electorales_de_cordoba():
    global ciudad, votos_validos, concejales, partidos_con_votos
    ciudad = "CÓRDOBA"
    votos_validos = 146548
    concejales = 29
    partidos_con_votos = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                          [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                          [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                          [161, "PUM+J"]]
    print("Datos de Córdoba cargados.")


def introducir_datos_electorales():
    global ciudad, votos_validos, concejales, partidos_con_votos
    comprueba_y_o_sobreescribe_datos(partidos_con_votos)
    ciudad = input("Escribe la localidad en la que se han realizado las elecciones:   ")
    votos_validos = input("Escribe los votos validos contabilizados:   ")
    concejales = input("Escribe el numero de concejales o ediles a repartir:   ")


def comprueba_y_o_sobreescribe_datos(partidos_polit_con_votos):
    if len(partidos_polit_con_votos) != 0:
        pregunta_sobreescribir = input("¿Existen datos guardados, desea sobreescribirlos? (S):  ")
        if pregunta_sobreescribir == 'S':
            partidos_polit_con_votos.clear()


def introducir_partidos_y_votos():
    global partidos, votos, partidos_con_votos
    partido_ya_introducido_o_supera_votos_totales = False
    votos_totales = comprueba_si_existen_datos(partidos, partidos_con_votos, votos)
    partidos, votos = comprueba_y_anade_partido_votos(partido_ya_introducido_o_supera_votos_totales, partidos, votos,
                                                      votos_totales)
    partidos_con_votos.clear()
    for i in range(len(partidos)):
        partidos_con_votos.append([votos[i], partidos[i]])


def comprueba_y_anade_partido_votos(partido_ya_introducido_o_supera_votos_totales, partidos_po, votos_po,
                                    votos_totales):
    while True:
        partido_a_anadir = input("Introduce el partido a añadir:    ")
        votos_a_anadir = int(input("Introduce los votos de dicho partido:   "))
        votos_parciales_totales = votos_totales + votos_a_anadir
        if partido_a_anadir in partidos_po or votos_parciales_totales > votos_validos:
            partido_ya_introducido_o_supera_votos_totales = True
            print("ERROR. NO PUEDES INTRODUCIR UN PARTIDO 2 VECES NI LA CANTIDAD DE VOTOS PUEDE SUMAR MAS QUE LA "
                  "CANTIDAD DE VOTOS TOTALES")
        if not partido_ya_introducido_o_supera_votos_totales:
            partidos_po.append(partido_a_anadir)
            votos_po.append(votos_a_anadir)
            break
    return partidos_po, votos_po


def comprueba_si_existen_datos(partidos_p, partidos_p_con_votos, votos_p):
    if len(partidos_p_con_votos) != 0:
        for x in range(len(partidos_p_con_votos)):
            partidos_p.append(partidos_p_con_votos[x][1])
            votos_p.append(partidos_p_con_votos[x][0])
    votos_totales = sum(votos_p)
    return votos_totales


def calcular_e_imprimir_simulacion():
    global votos, partidos, partidos_con_votos, concejales
    partidos_politicos = []
    votos_politicos = []
    lista_simula_votacion = []
    lista_no_simula_votacion = []
    resto = []
    ordena_votos = partidos_con_votos.copy()
    contador = 0
    porcentaje = []
    ordena_votos.sort()
    ordena_votos.reverse()
    for x in range(len(ordena_votos)):
        partidos_politicos.append(ordena_votos[x][1])
        votos_politicos.append(ordena_votos[x][0])

    ediles = [0] * len(votos_politicos)

    for x in range(len(votos_politicos)):
        porciento = round(((votos_politicos[x] * 100) / votos_validos), 2)
        porcent = str(porciento) + "%"
        porcentaje.append(porcent)
        if porciento >= 5.00:
            lista_simula_votacion.append([partidos_politicos[x], ediles[x], votos_politicos[x], porcent[x]])
        else:
            lista_no_simula_votacion.append([partidos_politicos[x], ediles[x], votos_politicos[x], porcent[x]])

    for x in range(len(lista_simula_votacion)):
        resto.append(lista_simula_votacion[x][2])

    while contador <= concejales:
        for x in range(len(resto)):
            candidato = resto[x]
            if candidato == max(resto):
                ediles[x] += 1
                resto[x] = int(resto[x]) // 2
                contador += 1


if __name__ == "__main__":
    main()

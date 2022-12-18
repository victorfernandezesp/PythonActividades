import math


def maximum(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    maximo = numeros[0]
    for i in numeros[1:]:
        if i > maximo:
            maximo = i
    return maximo


def minimum(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    minimo = numeros[0]
    for i in numeros[1:]:
        if i < minimo:
            minimo = i
    return minimo


def mean(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    longitud = len(numeros)
    acumulador = 0
    for i in numeros:
        acumulador += i
    media = acumulador / longitud
    return media


def variance(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    media = mean(numeros)
    varianza = 0
    for i in numeros:
        varianza += (i - media) ** 2
    varianza = varianza / len(numeros)
    return varianza


def median(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    numeros_ordenados = sorted(numeros)
    longitud = len(numeros_ordenados)
    if longitud % 2 != 0:
        mediana = float(numeros_ordenados[longitud // 2])
        return mediana
    else:
        parte_mediana_1 = numeros_ordenados[longitud // 2]
        parte_mediana_2 = numeros_ordenados[longitud // 2 - 1]
        mediana = float((parte_mediana_1 + parte_mediana_2) / 2)
        return mediana


def mode(*numeros):
    if len(numeros) == 1 and isinstance(numeros[0], (list, tuple)):
        numeros = numeros[0]
    numero_sale = []
    veces_que_sale = 0
    for i in numeros:
        cuenta = numeros.count(i)
        if cuenta > veces_que_sale:
            veces_que_sale = cuenta
            numero_sale.clear()
            if i not in numero_sale:
                numero_sale.append(i)
        elif cuenta == veces_que_sale:
            if i not in numero_sale:
                numero_sale.append(i)
    return numero_sale


if __name__ == "__main__":
    assert maximum(1, 2, 3, 4, 5, 6, 7) == 7
    assert maximum([1, 2, 3, 4, 5, 6, 7]) == 7
    assert minimum(1, 2, 3, 4, 5, 6, 7) == 1
    assert minimum([1, 2, 3, 4, 5, 6, 7]) == 1
    assert math.isclose(mean(1, 2, 3), 2)
    assert math.isclose(mean(1, 2, 6), 3)

    assert math.isclose(variance(8, -5, 4, 7, 6, 11, 10), 24.408163265306122)
    assert math.isclose(variance([8, -5, 4, 7, 6, 11, 10]), 24.408163265306122)

    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10), 7)
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10]), 7)

    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3) == [2]
    assert mode([1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3]) == [2]

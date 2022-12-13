import math


def maximum(*array):
    maximo = 0
    for i in array:
        if i > maximo:
            maximo = i
    return maximo


def minimum(*array):
    minimo = array[0]
    for i in array:
        if i < minimo:
            minimo = i
    return minimo


def mean(*array):
    longitud = len(array)
    acumulador = 0
    for i in array:
        acumulador += i
    media = acumulador / longitud
    return round(media, 2)


def variance(*array):
    media = mean(array)
    varianza = 0
    for i in array:
        varianza += (i - media) ** 2
    varianza = varianza / len(array)
    varianza = varianza ** 0.5
    return round(varianza, 2)


def median(*array):
    longitud = len(array)
    if longitud % 2 != 0:
        mediana = array[longitud // 2]
        return mediana
    else:
        parte_mediana_1 = array[longitud // 2]
        parte_mediana_2 = array[longitud // 2 - 1]
        mediana = (parte_mediana_1 + parte_mediana_2) / 2
        return mediana


def mode(*array):
    numero_sale = []
    veces_que_sale = 0
    for i in array:
        cuenta = array.count(i)
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
    assert math.isclose(mean(8, -5, 4, 7, 6, 11, 10), 5.857142857) == True
    assert math.isclose(mean([8, -5, 4, 7, 6, 11, 10]), 5.857142857) == True
    assert math.isclose(variance(8, -5, 4, 7, 6, 11, 10), 24.408163265306122) == True
    assert math.isclose(variance([8, -5, 4, 7, 6, 11, 10]), 24.408163265306122) == True
    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10), 7) == True
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10]), 7) == True
    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3) == [2]
    assert mode([1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3]) == [2]
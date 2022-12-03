"""
    Ejercicio 2:
        Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas
        dentro de otras si es necesario.

        Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho
        trabajo. Por ejemplo, la función es_capicua() resulta trivial teniendo voltea() y la función siguiente_primo()
        también es muy fácil de implementar teniendo es_primo().

        Prohibido utilizar funciones de conversión del número a una cadena.

        es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.

        es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.

        siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.

        digitos: devuelve el número de dígitos de un número entero.

        voltea: le da la vuelta a un número.

        digito_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de
        izquierda a derecha.

        posicion_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se
        encuentra, devuelve -1.

        quita_por_detrás: le quita a un número n dígitos por detrás (por la derecha).

        quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).

        pega_por_detras: añade un dígito a un número por detrás.

        pega_por_delante: añade un dígito a un número por delante.

        trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
        correspondiente.

        juntaNumeros: pega dos números para formar uno.

        Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from bibliotecafunciones.funciones_matematicas.funciones_matematicas_tema05_ej2 import voltea, es_capicua, digitos, \
    es_primo, siguiente_primo, quita_por_detras, pega_por_detras, junta_numeros, trozo_de_numero, quita_por_delante, \
    pega_por_delante, digito_n, posicion_de_digito


def introduce_parametro():
    x = int(input("Introduce el valor:  "))
    return x


numero = introduce_parametro()

print(f"Es capicua: {es_capicua(numero)}")
print(f"Es Primo: {es_primo(numero)}")
print(f"Siguiente Primo: {siguiente_primo(numero)}")
print(f"Digitos: {numero} tiene: {digitos(numero)} digitos")
print(f"Volteado: {voltea(numero)}")

print("Numero N, introduce la posicion y sacare el numero correspondiente: ")
posicion = introduce_parametro()
print(f"En la posicion {posicion} esta el numero: {digito_n(numero, posicion)}")


print("Posicion De Digito, introduce el numero y sacare la posicion correspondiente: ")
numero_introducido = introduce_parametro()
print(f"En numero {numero_introducido} esta en la posicion: {posicion_de_digito(numero, numero_introducido)}")

print("Quita por detras: Cuantos quito? ")
quito = introduce_parametro()
print(f"El numero con {quito} numero/os quitados de detras es: {quita_por_detras(numero, quito)}")

print("Quita por delante: Cuantos quito? ")
quito = introduce_parametro()
print(f"El numero con {quito} numero/os quitados de delante es: {quita_por_delante(numero, quito)}")

print("Pega por detras: ¿Que numero de un digito pego? ")
pego = introduce_parametro()
print(f"El numero con el numero {pego} pegado por detras es: {pega_por_detras(numero, pego)}")

print("Pega por delante: ¿Que numero de un digito pego? ")
pego = introduce_parametro()
print(f"El numero con el numero {pego} pegado por delante es: {pega_por_delante(numero, pego)}")

print(f"Trozo de Numero: El numero resultante de la primera posicion y la ultima posicion es : "
      f"{trozo_de_numero(numero)}")

print("JuntaNumeros: ¿Que numero quieres que junte? ")
junta1 = introduce_parametro()
junta2 = introduce_parametro()
print(f"El numero {junta1} juntado con el numero {junta2} da como resultado: {junta_numeros(junta1, junta2)}")

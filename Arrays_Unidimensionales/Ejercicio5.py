"""
    Ejercicio 5:
        Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre
        a continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a
        base de asteriscos o cualquier otro carácter.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

meses = []
mes = 1
nombre = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct",
          "Nov", "Dic"]

for i in range(12):
    temp = float(input(f"Escribe la temperatura que ha hecho en el mes {nombre[i]}: "))
    temp = "*" * int(temp)
    meses.append(temp)

for j in range(12):
    print(f"{nombre[j]}: {meses[j]}")
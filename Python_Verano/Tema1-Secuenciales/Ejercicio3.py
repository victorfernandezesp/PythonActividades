# 3.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# Autor: Victor Fernandez España
# En este programa calcularemos la hipotenusa de un triangulo rectángulo, primero recibiremos los valores por teclado,
# se calculara la hipotenusa y seguidamente se mostrara por pantalla

# Guardamos en las variables los valores con los que trabajaremos
cateto1 = float(input("Introduce el cateto numero 1 "))
cateto2 = float(input("Introduce el cateto numero 2 "))

# Resolvemos la hipotenusa
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

# Imprimimos resultados
print("La hipotenusa del triangulo es ", hipotenusa)

# 6. Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
# Author: Victor Fernandez España

# Introducimos por teclado el número con el que vamos a trabajar
cadena = str(input("Introduce una cadena por teclado: "))
print(f"-----------------------------------------------------------------")

# Realizamos las distintas operaciones
if len(cadena) == 1 and "a" <= cadena <= "z" or ("á" <= cadena <= "ú") or (cadena == "ñ" or cadena == "ü"):
    # Mostramos por pantalla los resultados
    print(f"La cadena es Minuscule ")
    # Mostramos por pantalla los resultados
elif len(cadena) == 1 and "A" <= cadena <= "Z" or ("Á" <= cadena <= "Ú") or (cadena == "Ñ" or cadena == "Ü"):
    # Mostramos por pantalla los resultados
    print(f"La cadena es Mayúscula ")
elif len(cadena) > 1:
    print(f"No has introducido un character valido, comprueba su longitud, tiene que ser 1.")

else:
    print(f"No has introducido un character valido")
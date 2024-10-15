"""
Bucles

while
contadores
acumuladores


# while + condicion + :

condicion = True

while condicion:
    check = input("Ingrese x para salir o cualquier tecla para continuar: ").lower()
    if check == "x":
        condicion = False


# contador
contador = 0

while contador < 10:
    print(contador)

    # incrementar el contador
    # contador = contador + 1  # contador tomar el valor 2
    contador += 1  # contador tomar el valor 2



contador = 0  # define la cantidad de veces que se ejecuta el Bucle
acumulador = 0  # almacenar la suma de los valores ingresados

while contador < 3:
    valor = float(input("Ingrese un número: "))
    acumulador = acumulador + valor
    print(f"acumulacion parcial: {acumulador}")
    contador += 1  # Siempre tiene que estar

print(f"acumulacion final: {acumulador}")
"""

"""
Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 


CANTIDAD_MESES = 6
contador_meses = 0
acumulador_sueldos = 0


print()

while contador_meses < CANTIDAD_MESES:
    contador_meses = contador_meses + 1
    ingreso = float(input(f"Ingrese el sueldo del mes {contador_meses}: "))
    acumulador_sueldos = acumulador_sueldos + ingreso
    print(f"sumar parcial {acumulador_sueldos} ")

promedio = acumulador_sueldos / contador_meses
print(f"\nEl ingreso promedio en el semestre es de {promedio}")



# Bucles y cadenas

cadena = "Python"
indice = 0  # hace las veces de un contador
print(cadena)

while indice < len(cadena):  # indice = 2 < len(cadena)=> 6
    # print(cadena[indice])
    print(f"cadena[{indice}]: {cadena[indice]}")

    indice += 1
"""

# Bucles y cadenas

cadena = "Python"
# quiero imprimir PyThOn
indice = 0  # hace las veces de un contador
print(cadena)

while indice < len(cadena):  # indice = 2 < len(cadena)=> 6
    # bloque de código que los indices pares imprima el caracter en mayuscula
    # y que los indice impares imprima en minuscula => usar %

    if indice % 2 == 0:  # estoy en indices pares
        print(cadena[indice].upper())
    else:
        print(cadena[indice].lower())
    indice += 1

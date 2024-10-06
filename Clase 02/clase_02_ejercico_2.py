"""
Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 

"""

# Entrada
print("Ingreso los ingresos correspondientes a los primeros 6 meses del año:")
# Guardar los ingresos de cada mes
ingreso_de_enero = int(input("Ingresos del mes de Enero: "))
ingreso_de_febrero = int(input("Ingresos del mes de Febrero: "))
ingreso_de_marzo = int(input("Ingresos del mes de Marzo: "))
ingreso_de_abril = int(input("Ingresos del mes de Abril: "))
ingreso_de_mayo = int(input("Ingresos del mes de Mayo: "))
ingreso_de_junio = int(input("Ingresos del mes de Junio: "))

# calcular el promedio
# sumar los ingresos de los 6 meses
# dividir por 6
suma = (
    ingreso_de_enero
    + ingreso_de_febrero
    + ingreso_de_marzo
    + ingreso_de_abril
    + ingreso_de_mayo
    + ingreso_de_junio
)

promedio = suma / 6

# Mostramos el promedio concatenando 2 strings (str)
print("El promedio de los ingresos es: " + str(promedio))

# Mostramos el promedio usando la coma, convierte automáticamente el tipo de dato a str
print("El promedio de los ingresos es: ", promedio)

# Mostramos el promedio usando f-string. El uso de float:.2f indica 2 decimales
print(f"El promedio de los ingresos es: {promedio:.2f}")

# Mostramos el promedio usando f-string y la función round (numero, cant_digitos)
print(f"La suma es {suma} y el promedio de los ingresos es: {round(promedio)}")

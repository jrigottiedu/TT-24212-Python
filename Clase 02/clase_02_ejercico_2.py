# Guardar los ingresos de cada mes
ingreso_de_enero = 1000
ingreso_de_febrero = 2000
ingreso_de_marzo = 1500
ingreso_de_abril = 1700
ingreso_de_mayo = 1660
ingreso_de_junio = 1900

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

print(
    "El promedio de los ingresos es: " + str(promedio)
)  # concatenando 2 strings (str)
print("El promedio de los ingresos es: ", promedio)  # la coma da formato al float
print(
    f"El promedio de los ingresos es: {promedio:.2f}"
)  # usando f-string float:.2f para indicar 2 decimales
print(
    f"La suma es {suma} y el promedio de los ingresos es: {round(promedio)}"  # usando la función round(numero, cant_digitos)
)  # usando f-string

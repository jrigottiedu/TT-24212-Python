"""
Desafío:Refactorizamos el código del Ejercio 2 - clase 2 
1. Incorporamos validación de datos
2. Incorporamos Tuplas
3. Incorporamos Listas


Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 
"""

# Declaración e inicialización de variables
CANTIDAD_MESES = 6  # la usamos como constante
contador_meses = 0  # contador
acumulador_sueldos = 0  # acumulador

print()  # print para generar un espacio en blanco

# Bucle while que se ejecuta tantas veces como sea CANTIDAD_MESES
while contador_meses < CANTIDAD_MESES:
    contador_meses = contador_meses + 1  # incrememtamos el contador
    ingreso = float(input(f"Ingrese el sueldo del mes {contador_meses}: "))
    acumulador_sueldos = acumulador_sueldos + ingreso  # acumulamos los ingresos mensuales
    print(f"sumar parcial {acumulador_sueldos} ")  # impresiones parciales

promedio = acumulador_sueldos / contador_meses  # calculamos el promedio
print(f"\nEl ingreso promedio en el semestre es de {promedio}")

"""
Desafío: refactorizamos el código del Ejercio 2 - clase 2 incorporando lo aprendido

Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 
"""

# Declaración e inicialización de variables
tupla_meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)
indice = 0
acumulador_sueldos = 0  # acumulador

print()  # print para generar un espacio en blanco

# Bucle while que se ejecuta tantas veces como sea CANTIDAD_MESES
while indice < len(tupla_meses):
    ingreso = float(input(f"Ingrese el sueldo del mes {tupla_meses[indice]}: "))
    acumulador_sueldos = acumulador_sueldos + ingreso  # acumulamos los ingresos mensuales
    print(f"sumar parcial {acumulador_sueldos} ")  # impresiones parciales
    indice += 1  # incrememtamos el indice

promedio = acumulador_sueldos / len(tupla_meses)  # calculamos el promedio
print(f"\nEl ingreso promedio en el semestre es de {promedio}")

# Mejorar el código para que solo se puedan ingresar montos cero o positivos

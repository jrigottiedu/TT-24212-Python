"""
Desafío:Refactorizamos el código del Ejercio 2 - clase 2 
1. Incorporamos validación de datos: con un while
2. Incorporamos Tuplas para que el programa nos muestre los meses del año
3. Incorporamos Listas: para almacenar los valore ingresados


Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 
"""

# Declaramos una lista para almacenar los ingresos
lista_ingresos = []
lista_ingresos.clear()  # Limpiar la lista en memoria

# Declaración e inicialización de variables
tupla_meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
)
contador_meses = 0  # contador
acumulador_sueldos = 0  # acumulador

print()  # print para generar un espacio en blanco

# Bucle while que se ejecuta tantas veces como sea CANTIDAD_MESES
while contador_meses < len(tupla_meses):
    ingreso = float(input(f"Ingrese el sueldo del mes {tupla_meses[contador_meses]}: "))
    # validar el ingreso
    while ingreso < 0:
        print("No se admiten ingresos negativos")
        ingreso = float(
            input(f"Ingrese el sueldo del mes {tupla_meses[contador_meses]}: ")
        )
    # guardamos el ingreso en una lista
    elemento = [tupla_meses[contador_meses], ingreso]
    lista_ingresos.append(elemento)
    # el ingreso validado se guarda en el acumulador
    acumulador_sueldos = (
        acumulador_sueldos + ingreso
    )  # acumulamos los ingresos mensuales
    print(f"sumar parcial {acumulador_sueldos} ")  # impresiones parciales
    contador_meses = contador_meses + 1  # incrememtamos el contador

promedio = acumulador_sueldos / len(tupla_meses)  # calculamos el promedio
print(f"\nEl ingreso promedio en el semestre es de {promedio}")

indice = 0
while indice < len(lista_ingresos):
    # print(f"\nLa lista de ingresos es: {lista_ingresos}")
    print(f"Mes: {lista_ingresos[indice][0]} - Ingreso: {lista_ingresos[indice][1]}")
    indice += 1

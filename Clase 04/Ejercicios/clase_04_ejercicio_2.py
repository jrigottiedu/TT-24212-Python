"""
Este ejercicio los hicimos juntos en el After Class del miércoles 2/10

Consumo de combustible

Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
muestra un detalle de los litros consumidos y el dinero gastado.  
"""

while True:
    # Declaración de variables
    consumo = None  # litros por cada 100 km ej: 10 litros (10 l/100 km)
    distancia_recorrida = None  # kms
    costo_combustible = None  # pesos por litro

    # Entrada
    print("Ingreso los valores solicitados:")
    consumo = float(input("Ingrese el consumo en litros (por cada 100 kms): "))
    distancia_recorrida = float(input("Ingrese la distancia recorrida en Kms: "))
    costo_combustible = float(input("Ingrese el precio del litro de combustible en pesos: "))

    # Proceso
    # litros_consumidos = (consumo * distancia_recorrida) / 100
    litros_consumidos = distancia_recorrida / consumo
    costo_recorrido = litros_consumidos * costo_combustible

    # Salida
    print(
        f"Si usted recorre {distancia_recorrida} kms, va a consumir {litros_consumidos:.2f} litros "
    )
    print(f"Y usted gasto {costo_recorrido:.2f} pesos")

    # detenemos el bucle con metodo 1
    # opcion = input("Para terminar ingrese una x").lower()  # str.lower() convierte a minúscula
    # if opcion == "x":
    #     break

    # detenemos el bucle con metodo 1
    opcion = input("Para terminar ingrese una x")  # str.lower() convierte a minúscula
    if opcion == "x" or opcion == "X":
        break

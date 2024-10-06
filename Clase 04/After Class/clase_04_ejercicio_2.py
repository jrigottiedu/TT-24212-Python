"""
Este ejercicio los hicimos juntos en el After Class del miércoles 2/10

Consumo de combustible

Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
muestra un detalle de los litros consumidos y el dinero gastado.  
"""

# Declaracion de variables
litros_consumidos = None  # Litros consumidos
costo_total = None  # costo en combustible
autonomia = None  # consumo cada 100Km (10 litros cada 100Km)
precio_combustible = None  # 1000 pesos el litro
distancia_recorrida = None  # 400 Km

while True:
    # Entrada
    distancia_recorrida = float(
        input("Ingrese la distancia recorrida en Kms: ")
    )  # esto nos da los litros consumidos en funcion de la autonomia
    autonomia = float(input("Ingrese la autonomía de su vehículos en litros/100kms: "))
    precio_combustible = float(input("Ingrese el precio del litro de combustible: "))

    # Proceso
    litros_consumidos = (
        autonomia * distancia_recorrida
    ) / 100  # litros/100kms * kms = litros

    """
    autonomia = 10litros / 100Kms
    distancia_recorrida = 400Kms
    litros_consumidos = 40 litros
    """
    costo_total = litros_consumidos * precio_combustible

    # Salida
    print(
        f"Se consumieron {litros_consumidos:.2f} litros y se gastaron ${costo_total:.2f} en total."
    )

    seguir = input("Ingrese X para salir o cualquier cosa para continuar")
    if seguir == "x":
        break

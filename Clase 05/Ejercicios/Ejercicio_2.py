"""
Compra con descuentos

Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de artículos que está comprando. 
El programa debe determinar el descuento aplicable según las siguientes reglas:
Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, aplica un descuento del 15%.
Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento o simplemente el monto original si no hay descuento.
"""

# Declarar variables


# Entrada
while True:
    monto_compra = float(input("\nIngrese el monto total de la compra: "))
    cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))

    # Proceso
    # Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, aplica un descuento del 15%.
    if cantidad_articulos >= 5 and monto_compra >= 10000:
        descuento = monto_compra * 0.15

    # Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
    if cantidad_articulos >= 3 and cantidad_articulos < 5:
        descuento = monto_compra * 0.10

    # Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
    if cantidad_articulos < 3:
        descuento = 0

    # Salida

    print(
        f"Por su compra usted recibe un descuento de {descuento} pesos, el total a abonar es de {monto_compra - descuento} pesos"
    )

    opcion = input("Presione cualquier tecla para continuar o 'x' para salir: ").lower()
    if opcion == "x":
        break

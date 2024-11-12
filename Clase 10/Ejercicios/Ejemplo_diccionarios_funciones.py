"""
Refactorizamos Clase 07 - Ejercicio 1

Registro de productos en un inventario

Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. 
El programa debe permitir que el usuario agregue productos a un "DICCIONARIO" hasta que decida no agregar más. 
Luego, deberás mostrar todos los productos ingresados al inventario.


Tips: 

Usá una lista para almacenar los productos, los que a su vez se guardarán en un diccionario.
Diseña la lista pensando en el TFI.

"""

# cual es la estructura del diccionario
# "nombre_producto": "",
# "precio_producto": "",
# "stock_disponible": "",
# "categoria":""

import os

# Declaracion de variables
inventario = []


# Declaracion de funciones


def clear_terminal():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux y macOS
    else:
        os.system("clear")


def agregar_productos():
    while True:
        nombre_producto = input("\nIngrese el nombre del producto: ")

        if not buscar_producto(nombre_producto):
            precio_producto = input("Ingrese el precio unitario: ")
            stock_producto = input("Ingrese el stock unitario: ")

            # armo un diccionario temporal
            producto = {
                "nombre_producto": nombre_producto,
                "precio_producto": precio_producto,
                "stock_disponible": stock_producto,
            }

            # inserto ese lista temporal en el inventario
            inventario.append(producto)
        else:
            print("El producto ya existe en el inventario")

        mas_productos = input("¿Desea agregar otro producto? (s/n): ")
        if mas_productos.lower() != "s":
            break


def buscar_producto(nombre_producto):
    for producto in inventario:
        if producto.get("nombre_producto") == nombre_producto:
            return True
    return False


def mostrar_productos():
    print("\nListado de productos:")
    if len(inventario) > 0:
        for producto in inventario:
            for clave, valor in producto.items():
                print(f"{clave}: {valor}")
    else:
        print("No hay productos en el inventario")


def mostrar_stock():
    print("\nStock de productos:")
    if len(inventario) > 0:
        for producto in inventario:
            print(
                f"\nProducto {producto.get("nombre_producto")} tiene un stock de {producto.get("stock_disponible")}"
            )
    else:
        print("No hay productos en el inventario")


while True:
    print()
    print("1. agregar producto")
    print("2. mostrar producto")
    print("3. ver stock")
    print("4. salir")

    opcion = input("Su opcion: ")

    if opcion == "1":
        agregar_productos()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        mostrar_stock()

    elif opcion == "4":
        break
    else:
        print("Opcion invalida")

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

"""
Estructura de lista
lista_producto[0] = nombre
lista_producto[1] = cantidad

Estructura de diccionario
diccionario_producto = {
"id": unico
"nombre": "manzana", 
"cantidad": 10
}
"""

import os

# Declaracion de variables lista
inventario = []  # lista principal

while True:
    print("1. agregar producto")
    print("2. mostrar inventario")
    print("3. salir")

    opcion = input("Su opcion: ")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_producto = input("Ingrese la cantidad del producto: ")

        # armo una lista temporal
        # lista_producto = [nombre_producto, cantidad_producto]
        diccionario_producto = {
            "nombre": nombre_producto,
            "cantidad": cantidad_producto,
        }

        # inserto ese lista temporal en el inventario
        inventario.append(diccionario_producto)

    elif opcion == "2":
        print("\n Inventario")

        for producto in inventario:  # iterar la lista principal
            # print(
            #     f"Producto: {producto["nombre"]} cantidad: {producto.get("quantity", 0)}"
            # )
            for items in producto.items():
                print(f"{items}")  # imprimir los valores del diccion
    elif opcion == "3":
        break
    else:
        print("Opcion invalida")

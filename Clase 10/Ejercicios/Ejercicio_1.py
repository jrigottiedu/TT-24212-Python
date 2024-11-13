"""
Gestión de inventario con diccionarios

En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:


Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario 
donde la clave es el nombre del producto y el valor es su precio.

Una vez ingresados, mostrará todos los productos y sus precios en pantalla.



Producto: queso, Precio: 100, vencimiento: 10/12, local: "palermo"
"queso" : 100
"queso" : "10/12"

Producto: yogurt, Precio: 150, vencimiento: 15/12 

Producto: flan, Precio: 120, vencimiento: 20/12
"""

# declaramos
inventario = {}  # diccionario


for p in range(3):  # range devuelve una lista numerica [0, 1, 2]
    producto = input(
        "Ingrese el nombre del producto: "
    )  # el nombre de producto es la clave del diccionario
    precio = input("Ingrese el precio del producto: ")
    vencimiento = input("Ingrese el vencimiento del producto: ")

    # guardo las propiedades de cada producto en una lista
    inventario[producto] = [
        precio,
        vencimiento,
    ]

    # guardo las propiedades de cada producto en un diccionario
    inventario[producto] = {"precio": precio, "vencimiento": vencimiento}


print(inventario)

for clave, valor in inventario.items():
    print(f"Producto: {clave}, Precio: {valor[0]}, Vencimiento {valor[1]}")

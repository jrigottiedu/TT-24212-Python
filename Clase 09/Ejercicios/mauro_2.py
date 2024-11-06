"""
Mostrar los códigos de productos ingresados

En un sistema de inventario, cada producto tiene un código que lo identifica.
Escribí un programa que permita ingresar los códigos de 4 productos y luego mostrálos uno por uno,
junto con su posición en la lista.

Ejemplo: si los códigos ingresados son "P001", "P002", "P003", "P004", el programa debe mostrar:  

Tips: 

Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.


"""

# id, producto, stock
productos = [
    ["001", "Camiseta básica", 25],
    ["002", "Pantalón vaquero", 15],
    ["003", "Chaqueta de cuero", 8],
    ["004", "Sudadera con capucha", 12],
    ["005", "Vestido floral", 20],
    ["006", "Zapatos deportivos", 30],
    ["007", "Sombrero de paja", 10],
    ["008", "Camisa de cuadros", 18],
    ["009", "Cinturón de cuero", 14],
    ["010", "Bufanda de lana", 22],
]
codigo_de_producto = int(
    input("\nAlta de Produnto, ingrese codigo de producto, o  0 para cancelar: ")
)
# bucle while para seguir ingresando mientras el codigo se != 0
while codigo_de_producto != 0:

    nombre_producto = input("Nombre de producto: ").upper()
    cantidad_producto = int(input("Cantidad: "))
    # Agrego los productos a una lista dentro de otra lista
    productos.append(
        [
            codigo_de_producto,
            nombre_producto,
            cantidad_producto,
        ]
    )

    # vuevo a pedir un nuevo codigo para saber si continua el ingreso o se cancela y vuelve al menu principal

    codigo_de_producto = int(input("ingrese codigo de producto, o  0 para cancelar:  "))

# buscar por id

for id in range(len(productos)):
    print(f"Producto {id} es el código: {productos[id][0]} ")

"""
Actualización del inventario a partir de un arreglo

En una tienda, es necesario actualizar el inventario cuando se venden productos. 
A continuación, te proporcionamos un arreglo con una lista de productos, 
donde cada producto tiene un código, una descripción y una cantidad en stock. 
Escribí un programa que permita:


Seleccionar un producto a partir de su código.

Ingresar la cantidad vendida (que debe ser mayor que cero).

Actualizar la cantidad en stock de ese producto restando la cantidad vendida.
"""

# codigo_producto, nombre, cantidad_stock
# productos es lista de listas
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

print("\nLista de productos", productos)
codigo_producto = input("\nIngrese el código del producto: ")
# tenemos que buscar el codigo 005 en la lista
no_encontrado = True
for producto in productos:
    # si el codigo existe
    if codigo_producto == producto[0]:
        # bloque True
        no_encontrado = False
        print(f"Producto {producto[1]} cantidad {producto[2]}")
        # le pido la cantidad y actualizo
        cantidad_vendida = int(input("Ingrese cantidad vendida: "))

        while cantidad_vendida > producto[2] or cantidad_vendida <= 0:
            print("ERROR: Cantidad incorrecta, por favor ingrese nuevamente.")
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

        producto[2] = producto[2] - cantidad_vendida

        print(f"Actualización: Producto {producto[1]} cantidad {producto[2]}")
        break

if no_encontrado:
    print("\n Código no encontrado")
# el codigo no existe
# informar que no existe

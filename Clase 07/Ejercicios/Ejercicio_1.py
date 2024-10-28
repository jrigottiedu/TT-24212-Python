"""
Clase 07 - Ejercicio 1

Registro de productos en un inventario

Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. 
El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más. 
Luego, deberás mostrar todos los productos ingresados al inventario.


Tips: 

Usá una lista para almacenar los productos.
Diseña la lista pensando en el TFI.
Pueden usar lista de listas, como vimos en el ejercicio de hoy "e_listas_tuplas_desafio.py"
"""

# cual es la estructura de la lista:
# 0: nombre_producto
# 1: precio_producto
# 2: stock_disponible
# 3: categoria


inventario = []

while True:
    print("1. agregar producto")
    print("2. mostrar producto")
    print("3. ver stock")
    print("4. salir")

    opcion = input("Su opcion: ")

    if opcion == "1":
        while True:
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = input("Ingrese el precio unitario: ")
            stock_producto = input("Ingrese el stock unitario: ")

            # armo una lista temporal
            lista_temporal = [nombre_producto, precio_producto, stock_producto]

            # inserto ese lista temporal en el inventario
            inventario.append(lista_temporal)

            mas_productos = input("¿Desea agregar otro producto? (s/n): ")
            if mas_productos.lower() != "s":
                break

    elif opcion == "2":
        indice = 0
        while indice < len(inventario):
            print(
                f" Nombre de producto: {inventario[indice][0]} precio: {inventario[indice][1]} stock {inventario[indice][2]}"
            )
            indice += 1
    elif opcion == "3":
        print("stock disponible")
        # pedir al usuario el nombre del producto  (str)
        # while para iterar el inventario
        # if para ver si esa sub-lista tiene el producto

        buscar_producto = input("Ingrese el nombre del producto: ")
        indice = 0
        producto_no_encontrado = True
        while indice < len(inventario):
            if inventario[indice][0] == buscar_producto:
                print(
                    f"El producto {buscar_producto} tiene {inventario[indice][2]} unidades"
                )
                producto_no_encontrado = False  # activo la bandera
                break  # termina el while
            indice += 1
        if producto_no_encontrado:
            print("El producto no existe")
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")


"""
# referencias
tupla_marcas = ("samsung", "apple", "lenovo")
lista_marcas = ["samsung", "apple", "lenovo"]

# Ejemplo con diccionarios
marcas = {"samsung": ["s20", "s21", "s22+"]}


inventario = []
"""

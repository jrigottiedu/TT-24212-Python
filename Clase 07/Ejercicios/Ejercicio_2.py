"""

Consultar el stock de productos


Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en stock. 
Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando que no está disponible.

Tips: 

Usá una lista para almacenar los productos en stock.

Permití que el usuario ingrese el nombre de un producto a consultar.

Recorre la lista con un bucle while para verificar si el producto está en stock.

También pueden usar el método lista.index(elemento_a_buscar)

"""

# Inventario de una tiena

# Declaracion de variables
inventario = []
inventario.clear()

while True:
    print("\nMenu\n")
    print("1. Alta de productos")
    print("2. Consultar Stock")
    print("3. Salir")
    opcion = input("\nIngrese su opción: ")

    if opcion == "1":
        print("\nAlta de productos, para terminar ingrese 'salir'")
        producto = input("Ingrese el nombre del producto o 'salir' para terminar: ")
        while producto.lower() != "salir":
            cantidad = input("Ingrese la cantidad de unidades: ")
            precio = input("Ingrese el precio unitario: ")
            inventario.append([producto, cantidad, precio])
            producto = input("Ingrese el nombre del producto o salir para terminar: ")

    elif opcion == "2":
        busqueda = input("Ingrese el nombre del producto a consultar: ")
        indice = 0
        valor_encontrado = False
        while indice < len(inventario):
            if inventario[indice][0].lower() == busqueda.lower():
                print("Producto \t\tUnidades \tPrecio")
                print(
                    f"{inventario[indice][0]} \t\t{inventario[indice][1]} \t\t{inventario[indice][2]}"
                )
            indice += 1
        if not valor_encontrado:
            print("\nProducto no encontrado\n")
    elif opcion == "3":
        break
    else:
        print("Entrada no válida!")

from funciones_database import *

# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************


# Funcion que muestra el menú
def menu_mostrar_opciones():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")
    # Agregan un modulo de validacion para evitar errores - PENDIENTE
    # retorno un Str
    return opcion


"""
menu_registrar_producto()

1. solicita al usuario el ingreso de los datos
2. *** valida los valores y tipos de datos ingresados
3. almacena los valores en un diccionario llamado producto
4. llama a db_insertar_producto(producto) y le pasa como argumento el diccionario producto para que lo inserte en la base de datos
"""


def menu_registrar_producto():
    print("\nIngrese los siguientes datos del producto:")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")

    # Ingreso y validacion de la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        # except ValueError:
        except Exception as error:
            # print(f"Error: debe ingresar un número entero")
            print(f"ERROR cantidad: {error}")

    # Validar el precio
    while True:
        try:
            # Codigo a testear
            precio = float(input("Precio: "))
            break
        except Exception as error:
            # Lo que hace cuando encuentra exception
            print(f"ERROR precio: {error}")

    # TO DO: VALIDAR VALORES Y TIPOS DE DATOS

    # Creamos un diccionario temporal
    # producto = {
    #     "nombre": nombre,
    #     "descripcion": descripcion,
    #     "categoria": categoria,
    #     "cantidad": cantidad,
    #     "precio": precio,
    # }

    # print("\n", producto)
    resultado = db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)
    if resultado == True:
        print("Registro insertado exitosamente!")
    else:
        print("Algo fallo")


"""
menu_mostrar_productos()

1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. si hay productos, los muestra en consola usando un bucle for
4. si no hay productos, muestra un mensaje indicando que no hay productos
"""


def menu_mostrar_productos():
    lista_productos = db_get_productos()  # retorna una lista

    if not lista_productos:
        print("No hay productos que mostrar")
    else:
        for producto in lista_productos:
            print(producto)


""""
def menu_actualizar_producto()

1. solicita al usuario que ingrese el id del producto a modificar
2. busca el producto en la tabla (si no existe informamos)
3. muestra la cantidad actual y solicita que ingrese la nueva cantidad
4. llama a db_actualizar_registro(id, nueva_cantidad) para que actualice la cantidad

"""


def menu_actualizar_producto():
    id = int(input("Ingrese el id del producto a actualizar"))
    producto = db_get_producto_by_id(id)
    if producto:
        print(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad"))
        db_actualizar_producto(id, nueva_cantidad)
        print("Cantidad actualizada exitosamente!")
    else:
        print("No existe el producto con el id ingresado")


"""
menu_eliminar_producto()

1. solicita al usuario que ingrese el id del producto a eliminar
2. busca el producto por el id en la tabla (si no existe informa)
3. muestra el producto y solicita confirmación
4. llama a db_eliminar_producto(id) para eliminar el registro con el id indicado
"""


def menu_eliminar_producto():
    id = int(input("Ingrese el id del producto a eliminar"))
    producto = db_get_producto_by_id(id)
    if producto:
        print(producto)
        db_eliminar_producto(id)
        print("Producto eliminado exitosamente!")
    else:
        print("No existe el producto con el id ingresado")


"""
menu_buscar_producto()
1. solicita al usuario que ingrese el id del producto a buscar
2. llama a db_get_producto_by_id(id)
3. si el producto existe lo muestra en consola, de lo contrario informa el error
"""


def menu_buscar_producto():
    id = int(input("Ingrese el id a buscar"))
    producto = db_get_producto_by_id(id)

    if not producto:
        print("No se ha encontrado el producto")
    else:
        print(producto)


"""
menu_reporte_bajo_stock()

1. solicita al usuario que ingrese la cantidad mínima de stock 
2. llama a db_get_productos_by_condicion(condicion) que retorna una lista_productos
3. si hay productos, los muestra en consola, de lo contrario informa
"""


def menu_reporte_bajo_stock():
    minimo_stock = int(input("Ingrese el minimo stock"))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos con stock menor a " + str(minimo_stock))

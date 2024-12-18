from funciones_database import *
from funciones_validacion import *

# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************


"""
menu_mostrar_opciones()
1. muestra en consola las opciones disponibles
2. captura y retorna la opcion seleccionada
"""


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
1. captura todos los datos
2. valida los datos y los almacena en un diccionario
3. llama a db_insertar_producto(producto) y le pasa el diccionario producto para que lo inserte en la base de datos
"""


def menu_registrar_producto():
    print("\nIngrese los siguientes datos del producto:")
    nombre = validacion_get_nombre()
    descripcion = validacion_get_descripcion()
    categoria = validacion_get_categoria()
    cantidad = validacion_get_cantidad()
    precio = validacion_get_precio()

    # Creamos un diccionario temporal
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insertar_producto(producto)
    print("\nProducto insertado exitosamente")


"""
menu_mostrar_productos()
1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. usamos un bucle for para mostrar en consola
"""


def menu_mostrar_productos():
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos que mostrar")


"""
menu_actualizar_producto()
1. solicita al usuario que ingrese el id del producto a modificar
2. buscamos el producto en la tabla (si no existe informamos)
3. mostramos cantidad actual y pedimos que ingrese la nueva cantidad
4. llamar a db_actualizar_registro(id, nueva_cantidad)

"""


def menu_actualizar_producto():
    id = int(input("\nIngrese el id del producto a actualizar"))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(f"Cantidad actual {get_producto[4]} ")
        nueva_cantidad = validacion_get_cantidad("Nueva cantidad")
        db_actualizar_producto(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")


"""
menu_eliminar_producto()
1. solicita al usuario que ingrese el id del producto a eliminar
2. buscamos el producto en la tabla (si no existe informamos)
3. mostramos el producto y solicitamos confirmación
4. llamar a db_eliminar_producto(id)
"""


def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print("Registro eliminado exitosamente!")
        else:
            print("Operación cancelada.")


"""
menu_buscar_producto()
1. solicita al usuario que ingrese el id del producto a buscar
2. llamar a db_get_producto_by_id(id)
"""


def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)


"""
menu_reporte_bajo_stock()
1. solicita al usuario que ingrese la cantidad mínima para el reporte
2. llamar a db_get_productos_by_condicion(condicion) que retorna una lista_productos
"""


def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)

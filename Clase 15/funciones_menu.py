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
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

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
    db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)
    print("Registro insertado exitosamente!")


"""
menu_mostrar_productos()

1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. si hay productos, los muestra en consola usando un bucle for
4. si no hay productos, muestra un mensaje indicando que no hay productos
"""


def menu_mostrar_productos():
    print("\n PENDIENTE DESARROLLO")
    # TO DO: DESARROLLAR SEGUN DESCRIPCION


""""
def menu_actualizar_producto()

1. solicita al usuario que ingrese el id del producto a modificar
2. busca el producto en la tabla (si no existe informamos)
3. muestra la cantidad actual y solicita que ingrese la nueva cantidad
4. llama a db_actualizar_registro(id, nueva_cantidad) para que actualice la cantidad

"""


def menu_actualizar_producto():
    print("\n PENDIENTE DESARROLLO")
    # TO DO: DESARROLLAR SEGUN DESCRIPCION


"""
menu_eliminar_producto()

1. solicita al usuario que ingrese el id del producto a eliminar
2. busca el producto por el id en la tabla (si no existe informa)
3. muestra el producto y solicita confirmación
4. llama a db_eliminar_producto(id) para eliminar el registro con el id indicado
"""


def menu_eliminar_producto():
    print("\n PENDIENTE DESARROLLO")
    # TO DO: DESARROLLAR SEGUN DESCRIPCION


"""
menu_buscar_producto()
1. solicita al usuario que ingrese el id del producto a buscar
2. llama a db_get_producto_by_id(id)
3. si el producto existe lo muestra en consola, de lo contrario informa el error
"""


def menu_buscar_producto():
    print("\n PENDIENTE DESARROLLO")
    # TO DO: DESARROLLAR SEGUN DESCRIPCION


"""
menu_reporte_bajo_stock()

1. solicita al usuario que ingrese la cantidad mínima de stock 
2. llama a db_get_productos_by_condicion(condicion) que retorna una lista_productos
3. si hay productos, los muestra en consola, de lo contrario informa
"""


def menu_reporte_bajo_stock():
    print("\n PENDIENTE DESARROLLO")
    # TO DO: DESARROLLAR SEGUN DESCRIPCION

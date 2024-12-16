"""
validacion_get_nombre()

1. Solicita el usuario que ingrese el nombre del producto
2. No se admite dato nulo
3. El nombre puede contener cualquier caracter
"""


def validacion_get_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("No se admite dato nulo. Ingrese el nombre: ")
        else:
            return nombre


"""
validacion_get_descripcion()

1. Solicita el usuario que ingrese la descripción del producto
2. Se admite dato nulo
3. La descripción puede contener cualquier caracter
"""


def validacion_get_descripcion():
    while True:
        descripcion = input("Descripción: ").strip()
        return descripcion


"""
validacion_get_categoria()

1. Solicita el usuario que ingrese la categoria del producto
2. No se admite dato nulo
3. La categoría puede contener cualquier caracter
"""


def validacion_get_categoria():
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("No se admite dato nulo. Ingrese la categoría: ")
        else:
            return categoria


"""
validacion_get_cantidad()

1. Solicita el usuario que ingrese la cantidad del producto
2. No se admite dato nulo
3. La categoría debe ser entero
"""


def validacion_get_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: ").strip())
            if not cantidad:
                print("No se admite dato nulo. Ingrese la cantidad: ")
            elif cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Ingrese la cantidad: ")
            else:
                return cantidad

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


"""
validacion_get_precio()

1. Solicita el usuario que ingrese el precio del producto
2. No se admite dato nulo
3. El precio debe ser entero o float
"""


def validacion_get_precio():
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if not precio:
                print("No se admite dato nulo. Ingrese el precio: ")
            else:
                return precio

        except ValueError:
            print("Tipo de dato no valido. Ingrese el precio: ")

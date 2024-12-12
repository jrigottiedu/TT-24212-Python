def validacion_get_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("No se admite dato nulo. Ingrese el nombre: ")
        else:
            return nombre


def validacion_get_descripcion():
    while True:
        descripcion = input("Descripción: ").strip()
        return descripcion


def validacion_get_categoria():
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("No se admite dato nulo. Ingrese la categoría: ")
        else:
            return categoria


def validacion_get_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if not cantidad:
                print("No se admite dato nulo. Ingrese la cantidad: ")
            else:
                return cantidad

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


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

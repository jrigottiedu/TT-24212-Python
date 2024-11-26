productos = []  # Lista donde guardar los productos
productos.clear()
# producto = {  # diccionario temporal para ingresar los datos
#     "nombre": "",
#     "stock": 0,
#     "id": "000",
# }
condicion = True
while condicion:
    nombre = input("Nombre del producto: ")  # ingreso el nombre
    stock = int(input("Ingrese el Stock: "))  # ingreso el stock
    id = input("Ingrese el código: ")  # ingreso el id

    # diccionario temporal para ingresar los datos
    producto = {"nombre": nombre, "stock": stock, "id": id}
    productos.append(producto)  # ingreso el diccionario temporal a la lista

    op = input(
        "Desea ingresar otro producto: S/N:\n"
    ).lower()  # pregunto si quiero ingresar otro producto
    if op == "n":  # si ingreso una 'n' salgo del while
        condicion = False
print("listado\n")
print(productos)  # imprimo la lista

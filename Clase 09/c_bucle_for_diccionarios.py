lista_productos = []

while True:
    nombre_producto = input("\nIngrese 0 para terminar o el nombre del producto: ")
    if nombre_producto == "0":
        break
    cantidad_producto = input("Ingrese la cantidad del producto: ")
    diccionario_temporal = {"nombre": nombre_producto, "cantidad": cantidad_producto}
    lista_productos.append(diccionario_temporal)

for producto in lista_productos:
    # print(f"{producto.get("nombre")} : {producto.get("cantidad")}")
    for clave, valor in producto.items():
        print(f"{clave} : {valor}")

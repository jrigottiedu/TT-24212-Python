"""
lista = []
tupla = ()
diccionario = {}

"""

lista_productos = []  # lista para persistencia
print(len(lista_productos))  # 0


while True:
    nombre = input("\ningrese nombre: ")
    descripcion = input("ingrese descripcion: ")
    precio = input("ingrese precio: ")

    if len(lista_productos) == 0:
        indice = 1
    else:
        ultimo_producto = lista_productos[-1]
        indice = ultimo_producto["id"] + 1

    # declaro e inicializo el diccionario con los datos ingresados
    producto = {
        "id": indice,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
    }  # {diccionario}
    lista_productos.append(producto)
    # llama a una funcion que va a persistir el diccionario en una BD
    # le van a pasar como argumento el diccionario

    opcion = input("Ingrese 's' para salir: ")
    if opcion.lower() == "s":
        break

print(lista_productos)
lista_productos.pop(1)  # elimina el elemento con indice 1
print(lista_productos)


# Iteramos la lista_productos
# for producto in lista_productos:
#     print(producto)

# Diccionarios
# Pares clave-valor

diccionario_productos = {"nombre": "manzana", "cantidad": "10"}
print(diccionario_productos["nombre"])
print(diccionario_productos.get("cantidad"))

diccionario_productos["precio"] = "500"

for clave in diccionario_productos:
    print(f"{clave}: {diccionario_productos.get(clave)}")

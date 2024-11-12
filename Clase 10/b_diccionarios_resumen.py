"""
Variables vista durante el curso:

Simples
str
int
float
bool

Complejas
lista = ["elemento1", "elemento2"]  un ídice por valor
tuplas = ()  un ídice por valor

*** diccionarios *** 
    parejas/pares clave-valor
    clave es única por lo cual tendremos un valor por clave
"""

# Declarar un diccionario
diccionario = {}
print(diccionario)

# Declarar e inicializar un diccionario
diccionario = {
    "nombre_producto": "manzana",
    "cantidad_producto": 10,
}

# Acceder a un valor en un diccionario [] y .get()
print("\nAccediendo a los datos del diccionario con []")
print(diccionario["nombre_producto"])
print(diccionario["cantidad_producto"])

print("\nAccediendo a los datos del diccionario con get")
print(diccionario.get("nombre_product", "No existe"))

# Actualizar un valor en un diccionario [] y .update()
print("\nActualizando el valor del diccionario con []")
print(diccionario)
diccionario["cantidad_producto"] = 20
print(diccionario)

print("\nActualizando el valor del diccionario con update")
print(diccionario)
diccionario.update({"cantidad_producto": 30})
print(diccionario)

# Agregar un valor en un diccionario []
print("\nAgregar un valor al diccionario con []")
print(diccionario)
diccionario["precio_producto"] = 5.99
print(diccionario)

# Remover un valor en un diccionario del y .pop()
print("\nRemover un valor del diccionario con del")
print(diccionario)
del diccionario["precio_producto"]
print(diccionario)

print("\nRemover un valor del diccionario con pop")
# print(diccionario)
# test_pop = diccionario.pop("cantidad_producto", "Clave inexistente")
# print(test_pop)
# print(diccionario)

# Iteramos el diccionario
print("\n Iteramos el diccionario con for")
for clave in diccionario:
    print(diccionario[clave])

print("\n Iteramos el diccionario con for y keys()")
for clave in diccionario.keys():
    print(diccionario[clave])

print("\n Iteramos el diccionario con for y values()")
for valor in diccionario.values():
    print(valor)

print("\n Iteramos el diccionario con for y items()")
# for item in diccionario.items():
#     print(f"{item[0]} {item[1]}")

for clave, valor in diccionario.items():
    print(f"{clave} {valor}")

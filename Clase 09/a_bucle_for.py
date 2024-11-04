"""
Bucle For

Estructura 
for variable_temporal in variable_iterar:
    print(variable)
   
Que cosas son iterables?
cadena str
lista => while / for
tupla  => while / for

*diccionario  => for

indice = 0
while indice < valor :
    codigo que se ejecuta mientras condicion es True
    
    indice += 1
"""

"""
cadena = "Python"
lista = ["Python", "Java", "Java Script", "Solidity"]

print(f"cadena: {cadena}")
print(f"lista: {lista}")

print()

tupla = ("enero", "febrero", "marzo")

print("\nIteramos cadena")
for caracter in cadena:
    print(caracter)

print("\nIteramos lista")
for elemento in lista:
    print(elemento)

print("\nIteramos tupla")
for mes in tupla:
    print(mes)


# En la preentrega, ingresabamos nombre y cantidad de cada producto

lista_productos = [["manzana", "10"], ["durazno", "20"]]

# while True:
#     nombre_producto = input("Ingrese 0 para terminar o el nombre del producto: ")
#     if nombre_producto == "0":
#         break
#     cantidad_producto = input("Ingrese la cantidad del producto: ")
#     lista_productos.append([nombre_producto, cantidad_producto])

for producto in lista_productos:
    # print(f"Producto: {producto[0]} - Cantidad {producto[1]}")
    for item in producto:
        print(item)


# range
# Imgresar los salarios del primer trimestre
tupla = ("enero", "febreo", "marzo")
lista_ingresos = []
for indice_mes in range(3):
    ingreso_temporal = float(input(f"Ingrese el salario de {tupla[indice_mes]}: "))
    lista_ingresos.append([tupla[indice_mes], ingreso_temporal])

for ingreso in lista_ingresos:
    print(f"Ingreso de {ingreso[0]}: {ingreso[1]}")
"""

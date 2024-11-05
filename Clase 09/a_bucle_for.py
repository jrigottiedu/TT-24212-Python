"""
Bucle For

Que cosas son iterables
listas
tuplas
str
diccionarios
slice de lista (sub lista)


cadena = "Python"
indice = 0
print("\nWHile")
while indice < len(cadena):
    # print(indice)
    print(cadena[indice])
    indice += 1

print("\nFOR")
for variable_temporal in cadena:  # variable_temporal === cadena[indice]
    print(variable_temporal)

bandera = True
while True:
    dato = input("Ingrese x para salir")
    if dato == "x":
        break


lista = ["manzana", "pera", "kiwi"]
for fruta in lista:
    print(fruta)
    if fruta == "pera":
        break



productos = [["manzana", 10], ["pera", 20], ["kiwi", 25]]  # Lista de listas

for (
    producto
) in (
    productos
):  # producto es una variable temporar que toma en cada iteracion el valor de cada componente de la lista que itero
    print(producto[0])  # manzana, pera, kiwi
    print(f"Producto {producto[0]} - cantidad {producto[1]}")  # manzana, pera, kiwi

    

# queremos ingresar los primeros 3 sueldos del año

# mes = 0
# while mes < 3:
#     sueldo = float(input("Ingrese el sueldo del mes "))
#     mes += 1


lista = [0, 1, 2]
indice = 0
while indice < len(lista):  # len(lista) devuelve 3 , indices 0,1,2
    print("while imprime lista", lista[indice])
    indice += 1


lista = [0, 1, 2]
# for mes in lista:  # range devuelve una lista numerica q tiene fin
for mes in lista:  # range devuelve una lista numerica q tiene fin
    print("mes con lista: ", mes)
"""

lista_frutas = ["manzana", "pera", "kiwi", "durazno", "melon"]

print("\nFor in lista_frutas")
for fruta in lista_frutas:
    print(fruta)  # imprime manzana, pera, kiwi, dur

print("\nFor in range(len(lista_frutas))")
for indice in range(len(lista_frutas)):  # range(3) genera lista = [0, 1, 2, 3]
    # print("indice con range: ", indice)
    print(f"Fruta[{indice}]: {lista_frutas[indice]}")

print("\nFor in enumerate(lista_frutas)")
for indice, fruta in enumerate(lista_frutas):
    print(f"Fruta[{indice}]: {fruta}")

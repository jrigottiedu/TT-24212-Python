# Metodos de listas
lista = ["manxana", 10, "pera", "kiwi"]

# agregar otro elemento a la lista
lista.append("durazno")
lista.append(10)
print(lista)

print()
indice = 0
while indice < len(lista):
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1
print()

# remover elemento con remove
lista.remove(10)
print("\nLista despues de remover el 10", lista)

indice = 0
while indice < len(lista):
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1

# remover o quitar elementos con pop
lista.pop()  # remover el último elemento
print(lista)

lista.pop(2)  # remover el último elemento
print(lista)


# mutabilidad e inmutabilidad
# los tipos de dato int son inmutables
numero = 1
numero = 2
numero = 3

# los tipos de dato lista son mutables
lista = [1, 2, 3]
lista.append(4)

# Conclusión
# en las líneas 36 y 37, cuando asigno los valores 2 y 3 a numero, en realidad se crea una nueva variable
# y la original luego se eliminar con el Garbage Collector

# en la línea 40 creo la variable lista con los elementos: 1, 2, 3
# en la línea 41, el método append modifica la misma variable, por ello el concepto de Mutabilidad

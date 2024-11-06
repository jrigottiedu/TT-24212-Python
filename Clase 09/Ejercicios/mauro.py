que_numero = int(input("Ingrese un numero entero positivo: "))
print("~" * 40)
suma = 0
for numero in range(1, que_numero + 1):
    suma = numero + suma

print("")
print("-" * 40)
print("La suma de los numeros es :", suma)
print("-" * 40)
print("")

# entrada
numero_1 = int(input("ingrese el numero 1: "))
numero_2 = int(input("ingrese el numero 2: "))

print("seleccione la operación a realizar:")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")

opcion = input("su elección es: ")  # opcion es del tipo str -> opcion = "1"
print(f"su opción fue: {opcion}")

# proceso
# suma = numero_1 + numero_2
# resta = numero_1 - numero_2
# multiplicacion = numero_1 * numero_2
# division = numero_1 / numero_2

# salida
if opcion == "1":  # comparar si opcion es igual al número 1
    suma = numero_1 + numero_2
    print(f"el resultado de la suma es: {suma}")
elif opcion == "2":
    resta = numero_1 - numero_2
    print(f"el resultado de la resta es: {resta}")
elif opcion == "3":
    multiplicacion = numero_1 * numero_2
    print(f"el resultado de la múltiplicación es: {multiplicacion}")
elif opcion == "4":
    division = numero_1 / numero_2
    print(f"el resultado de la división es: {division}")
else:
    print("no es un número valido")

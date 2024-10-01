"""
Operadores relacionales o de comparación
> mayor
>= mayor o igual
< menor
<= menor o igual
== igual
!=

NO existe ===
"""

numero = None  # solo para declarar
NUMERO_CONSTANTE = 50  # int
numero_1 = 50  # int
numero_2 = "50,2"  # str
flag_1 = True
flag_2 = False

print(f"tipo de dato de flag_1 es: {type(flag_1)}")

"""
memoria:
50 ocupan 2 espacios
50.25 ocupa 4 espacios
"""

print(f"el tipo de dato de numero_1 es  {type(numero_1)}")
print(f"el tipo de dato de numero_2 es  {type(numero_2)}")
print(f"comparo numero_1 es igual a numero_2: {numero_1 == numero_2}")
numero_1 = "70"  # str
NUMERO_CONSTANTE = 70  # int
print(f"el tipo de dato de numero_1 despues de la reasignación es:  {numero_1}")
print(
    f"el tipo de dato de NUMERO_CONSTANTE despues de la reasignación es:  {NUMERO_CONSTANTE}"
)

a = 20
b = 20
print(f"comparamos a > b, resulado: {a > b}")
print(f"comparamos a < b, resulado: {a < b}")
print(f"comparamos a mayor o igual b, resulado: {a >= b}")
print(f"comparamos a menor o igual b, resulado: {a <= b}")
print(f"comparamos a == b, resulado: {a == b}")  # comparamos por igual
print(f"comparamos a != b, resulado: {a != b}")  # comparamos por distinto

print(f"suma de a + b {a+b}")
print(f"division de a / b {a/b}")


"""
Operadores lógicos
and
or
not
"""

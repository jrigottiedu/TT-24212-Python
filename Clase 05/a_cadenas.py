"""
Cadenas de texto (string)
"""

# delimitador
cadena = 'Mi libro favorito es "El Principito"'
print(cadena)
cadena = "This is Juan's book"
print(cadena)


# operador *
print(2 * 3)
print("-" * 30)


# operador +
var1 = 1  # int
var2 = 2  # int
var3 = "3"  # str
var4 = "4"  # str

print(var1 + var2)
print(var3 + var4)
print(var1 + int(var4))


# longitud
cadena = "Aprendeiendo Python"
# print(len(cadena))
for i in range(len(cadena)):
    print(f"cadena[{i}] = {cadena[i]}")

# print(cadena[2])

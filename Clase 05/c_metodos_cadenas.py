"""
Métodos adicionales de cadenas
"""

cadena = "aprendiendo pYtHoN "
print(cadena.lower())  # convertir cadena a minúscula
print(cadena.upper())  # convertir cadena a mayúscula
print(cadena.title())  # convertir cadena a (capitalize)
print(cadena.capitalize())  # convertir cadena a título

number = 10.5
print("round(10.5)", round(number))
print("el indice del espacio es: ", cadena.find(" "))  # me devuelve indice = 11
print(cadena[cadena.find(" ") + 1 :])

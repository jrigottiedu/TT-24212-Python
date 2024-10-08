"""
Operadores lógicos
(Vimos operadores aritméticos y lo relacionales)

Operadores aritméticos => Operaciones matemáticas (+ - * / // % **)
Operadores relacionales (>, >=, . !=, <, <=) + operadores lógicos => Condicionales

operadores lógicos
and => Y 
or => O
not => Negación
"""

_5 = 5
_2 = 2
_3 = 3

print(_3 < _5 or _2 > _3)  # True OR False
print(_3 < _5 and not _2 > _3)  # True AND (not False) = True

opcion = False
while not opcion:
    ingreso = input("¿Desea continuar? (S/N)").lower()
    if ingreso == "s":
        opcion = True
    else:
        opcion = False

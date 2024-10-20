"""
Colecciones / Arreglos

TUPLS

"""

tupla_vacia = ()


tupla = ("Enero", "Febrero", "Marzo")  # constante
tupla = ("Abril", "Mayo", "Junio")  # constante
print(tupla)
print()
print(tupla[1])

# tupla[0] = "enero"  # No esta soportado
# tupla.append("Abril")

indice = 1
while indice < len(tupla):
    print(tupla[indice])
    indice += 1

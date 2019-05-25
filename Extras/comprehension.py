"""
lista = []

for x in range (101):
	lista.append(x)

print(lista)
"""

# estructura = [x for x in range(0,100)]
estructura = tuple( (x for x in range(0,101) 
						if x % 2 ==0
							if x < 50) )
print(estructura)

diccionario = { indice:valor
				for indice, valor in enumerate(estructura)}
print(diccionario)
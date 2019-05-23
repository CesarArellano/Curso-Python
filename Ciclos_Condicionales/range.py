"""
for valor in range(10):
	print(valor)

for valor in range(1,11):
	print(valor)

for valor in range(1,101,2):
	print(valor)

for valor in range(len(lista)):
	print("indice:",valor,"valor:",lista[valor])
"""

lista = [1,2,3,4,5,6]

for indice, valor in enumerate(lista,10):
	print("indice:",indice,"valor:", valor)
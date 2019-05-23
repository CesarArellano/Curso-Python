numeros = [1,2,3,4,5,6,7,8,9,10]
diccionario = {'a':1, 'b':2}

for llaves in diccionario: #Imprime llaves
	print(llaves)

for numero in numeros: #Imprime numeros
	print(numero)

valores = ( (10,20,30), ["strings", "strings2","strings3"], (True,False,True))
for valor1, valor2, valor3 in valores:
	print(valor1,valor2,valor3)

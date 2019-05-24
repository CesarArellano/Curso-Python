def suma(parametro_requerido, *args): #args es una tupla que recibe n parámetros.
	total = 0
	print(parametro_requerido)
	for valor in args:
		total+=valor
	return total

def usuarios_autenticados(**kwargs):
	print(kwargs)

resultado = suma("Esto es un argumento requerido",10,20,30,40,50,60)
print(resultado)

usuarios_autenticados(Cesar=True,Benito=False)
def tabla_multiplicar(numero, maximo = 10):
	"""Funcion que multiplica un número por la posicion"""
	for posicion in range(1,maximo+1):
		yield numero * posicion, numero, posicion

for resultado, num, pos in tabla_multiplicar(9,20):
	print(num,"x",pos,"=",resultado)
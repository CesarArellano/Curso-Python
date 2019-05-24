def comenzar_play_list(lista):
	def reproducir():
		nonlocal lista # Hace que el parámetro y la variable declarada en la funcion anidada sean igules.
		lista = [1,2,3]
		for val in lista:
			print(val)
	reproducir()
	print(lista)

lista = ['track 1', 'track 2','track 3']
comenzar_play_list(lista)
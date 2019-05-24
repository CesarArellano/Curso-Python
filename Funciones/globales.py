animal = 'Ballena' #Variable global

def mostar_animal():
	global animal # Se puede utilizar, modificar, eliminar las variables globales declaras aquí.
	animal = 'Leon' # Nueva variable aunque tenga el mismo nombre / propio namespace.
	print(animal)

mostar_animal()
print(animal)
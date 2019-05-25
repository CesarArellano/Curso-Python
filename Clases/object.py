class Gato:  #Llamando implicitamente a object
	def __init__(self,nombre=''): # Visualiza dirección de memoria.
		self.nombre = nombre
	def __str__(self): # Ahora visualiza lo que retorne.
		return self.nombre 

class Pato(object): #Llamando explicitamente a object
	def __init__(self,nombre=''):
		self.nombre = nombre

gato = Gato("Bigotes")
pato = Pato("Lucas")

print(gato.__dict__)
print(pato)
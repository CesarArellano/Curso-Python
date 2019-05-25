class Animal:
	def __init__(self,nombre=''):
		self.nombre = nombre
	def comer(self):
		print("Comiendo")

	def dormir(self):
		print("Durmiendo")

class Perro(Animal): #Perro hereda los atributos de la clase Animal

	def ladrar(self):
		print("Ladrando")

class Gato(Animal): #Gato hereda los atributos de la clase Animal
	
	def ronroneo(self):
		print("Ronroneo")

print("Perro:")
Layla = Perro("Layla")
Layla.ladrar()
Layla.comer()
Layla.dormir()

print("Gato:")
Gardfield = Gato()
Gardfield.ronroneo()
Gardfield.comer()
Gardfield.dormir()
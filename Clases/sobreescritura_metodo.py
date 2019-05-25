class Animal:
	def comer(self):
		print("Comiendo")
	def dormir(self):
		print("Durmiendo")
	def comun(self):
		print("Es un animal")

class Mascota:
	def __init__(self,nombre=''):
		self.nombre = nombre
	def fecha_adopcion(self,fecha):
		self.fecha_adopcion = fecha
	def mostrar_nombre(self):
		print("Tu mascota es: "+self.nombre)
	def comun(self):
		print("Es una mascota")
	
class Perro(Animal, Mascota): #Perro hereda los atributos de la clase Animal

	def ladrar(self):
		print("Ladrando")
	def comun(self):
		print("Es un perro")
	def dormir(self): # Sobre escritura de métodos
		print(self.nombre,"está Durmiendo")
		Animal.dormir(self) # Indica la clase donde está el método a ejecutar.
		print("No molestar")

print("Perro:")
Layla = Perro("Layla") # Layla es un objeto de tipo Perro
Layla.dormir()


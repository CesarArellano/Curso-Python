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

class Gato(Animal, Mascota): #Gato hereda los atributos de la clase Animal
	
	def ronroneo(self):
		print("Ronroneo")

print("Perro:")
Layla = Perro("Layla") # Layla es un objeto de tipo Perro
Layla.mostrar_nombre()
Layla.fecha_adopcion("Hoy")
Layla.comun()
print(Layla.fecha_adopcion)

print("Gato:")
Garfield = Gato("Garfield") # Gardfield es un objeto de tipo Gato
Garfield.comun()
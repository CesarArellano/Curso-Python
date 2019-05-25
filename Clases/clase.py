class Usuario:
	
	def crear_nombre(self,nombre): 
		self.nombre = nombre

	def saluda(self,nombre):
		return ("Hola, soy un usuario " + nombre) 

	def mostrar_username(self):
		print(self.username)

	def mostrar_nombre(self):
		print(self.nombre)

cesar = Usuario() 
cesar.username = 'César'
cesar.correo = 'cesarmauricio.arellano@gmail.com'

jaqueline = Usuario()
jaqueline.username = 'Jaqueline'
jaqueline.correo = 'jaqui.mexicano@gmail.com'

cesar.crear_nombre("César Arellano")
cesar.mostrar_nombre()
jaqueline.mostrar_username()
print(cesar.saluda("César"))
print(jaqueline.saluda("Jaqueline"))
print(type(cesar))
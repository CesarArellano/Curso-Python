## Codigo mejorado
class Usuario:
	
	def __init__(self, username='', nombre='', correo=''):
		self.username = username
		self.nombre = nombre
		self.correo = correo
	def saluda(self):
		return ("Hola, soy un usuario " + self.nombre) 

	def mostrar_username(self):
		print(self.username)

	def mostrar_nombre(self):
		print(self.nombre)

cesar = Usuario("César", "César Arellano", "raywayday@gmail.com") 
jaqueline = Usuario("Jaqueline", "Jaqueline Martínez", "jaqui.mexicano@gmail.com")

cesar.mostrar_nombre()
jaqueline.mostrar_username()

print(cesar.saluda())
print(jaqueline.saluda())
print(type(cesar))
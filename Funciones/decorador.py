#a, b, c
#a(b) -> c
# pass ndica que una funcion, ciclo o condición no va a ser nada todavía.

def decorador(funcion):

	def nueva_funcion(*args,**kwargs):
		print("Podemos agregar codigo antes")
		resultado = funcion(*args,**kwargs)
		print("Podemos agregar código después")
		return resultado

	return nueva_funcion


@decorador
def funcion_a_decorar():
	print("Este es una funcion a decorar")

@decorador
def suma(val1, val2):
	return val1 + val2

funcion_a_decorar()
print("\n")
resultado = suma(10,20)
print (resultado)
class Triangulo:

	numero = 2

	@staticmethod #No es necesario instanciar
	def area(base, altura):
		return (base * altura) / Triangulo.numero

resultado = Triangulo.area(10,20)
print(resultado)
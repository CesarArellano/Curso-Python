class Circulo:
	pi = 3.14159265 # variable de clase
	def __init__(self,radio):
		self.radio = radio # variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100 

print(circulo_a.radio)
print(Circulo.pi)
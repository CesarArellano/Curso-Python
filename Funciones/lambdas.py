mi_funcion = lambda grados=32 : grados * 1.8 + 32

resultado = mi_funcion()
print(resultado)

""" Otra forma de resolver.
def centigrados_a_farhenheit(grados):
	return grados * 1.8 + 32

funcion_variable = centigrados_a_farhenheit #Asignar a una variable una función.
resultado = funcion_variable(32)
print(resultado)
"""

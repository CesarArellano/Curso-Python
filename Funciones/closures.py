def mostrar_mensaje(mensaje):
	mensaje = mensaje.title()
	mensaje = mensaje.center(50," ") #local
	def mostrar():
		print(mensaje)
	return mostrar

nueva_funcion = mostrar_mensaje("césar arellano")
nueva_funcion()
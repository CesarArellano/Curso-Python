def crear_usuario(nombre, apellido, edad=18):
	return {
		'nombre' : nombre,
		'apellido' : apellido,
		'nombre_completo' : "{} {}".format(nombre,apellido),
		'edad': edad
	}

# diccionario =  crear_usuario("César Mauricio","Arellano Velásquez",19) Forma ordenada
diccionario = crear_usuario(edad=19, nombre="César", apellido="Arellano") # No importa el orden de los parametros, se ordena como debe ser.

print(diccionario['nombre'])
print(diccionario['apellido'])
print(diccionario['nombre_completo'])
print(diccionario['edad'])

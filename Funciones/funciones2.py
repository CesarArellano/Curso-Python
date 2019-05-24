def crear_mensaje(nombre):
	mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre)
	return mensaje

def suma(val1, val2, val3):
	return val1 + val2 + val3

def obtener_curso():
	return "Curso de Python","Básico", 3.6

nuevo_mensaje = crear_mensaje("Cesar")
print(nuevo_mensaje)

suma_total = suma(10,20,30)
print("La suma es:",suma_total)

curso, nivel, version = obtener_curso()
print(curso,nivel,version)

lista = obtener_curso()
print(lista)

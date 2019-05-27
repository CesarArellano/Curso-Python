num = 1
cantnum = 0

while num!=0:
	num = int(input("Ingrese un número (0 para salir)\n"))
	if num!=0:
		cantnum+=1

print("Cantidad de números leídos: {}".format(cantnum))

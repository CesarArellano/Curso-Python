num = 0
mayor = 0
while num != -99:
	num = int(input("Introduce un numero\n"))
	if num > mayor:
		mayor = num

print("El número mayor es: {}".format(mayor))
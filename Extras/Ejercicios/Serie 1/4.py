numprimo = int(input("Ingrese el número\n"))
cont = 0

for i in range (1, numprimo + 1):
	if numprimo % i == 0:
		cont+=1

if cont == 2 :
	print("El número {} es primo".format(numprimo))
else:
	print("El número {} no es primo".format(numprimo))
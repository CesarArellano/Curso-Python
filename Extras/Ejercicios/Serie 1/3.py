num1 = float(input("Ingrese el primer numero 1\n"))
num2 = float(input("Ingrese el primer numero 2\n"))
num3 = float(input("Ingrese el primer numero 3\n"))
num4 = float(input("Ingrese el primer numero 4\n"))

if(num1 > num2 and num1 > num3 and num1 > num4):
	print("El número mayor es: %d"%(num1))

if(num2 > num1 and num2 > num3 and num2 > num4):
	print("El número mayor es: %d"%(num2))

if(num3 > num1 and num3 > num2 and num3 > num4):
	print("El número mayor es: %d"%(num3))

if(num4 > num1 and num4 > num2 and num4 > num3):
	print("El número mayor es: %d"%(num4))
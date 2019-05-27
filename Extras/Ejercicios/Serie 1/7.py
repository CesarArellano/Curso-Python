a = int (input("Ingrese un número para el valor A:\n"))
b = int (input("Ingrese un número para el valor B:\n"))
c = int (input("Ingrese un número para el valor C:\n"))

temp = a
a = c
c = b
b = temp

print("Imprimir nuevos valores:\nValor A: {}\nValor B: {}\nValor C: {}".format(a,b,c))
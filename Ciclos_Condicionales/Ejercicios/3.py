"""
* @file 3.py
*
* @brief Crear una lista la cual almacene 10 números positivos ingresados
* por el usuario, mostrar en pantalla: la suma de todos los números,
* el promedio, el número mayor y el número menor.
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

import os
lista = []
numero=0
suma= 0

while numero!=10:
	num = float(input("¿Ingrese el numero %d a insertar en la lista?\n"%(numero+1)))
	if num > 0:
		lista.append(num)
		numero += 1
	else:
		print("Error, ingresa un numero positivo mayor a 0")

os.system ("clear") 
print("Los numeros ingresados son:")
for i in range(0,len(lista)):
	suma += lista[i]

print("La suma de los números es: %.3f"%(suma))
print("El promedio es: %.3f"%(suma/10))
print("El número mayor es: %.3f"%(max(lista)))
print("El número menor es: %.3f"%(min(lista)))
"""
* @file 7.py
*
* @brief Mostrar en pantalla la cantidad de vocales que existe en una
* frase dada por el usuario.
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

frase = input("Ingrese la frase\n")
cant = 0

for letra in frase:
	if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':  
		cant += 1
	if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':  
		cant += 1

print("Cantidad vocales:",cant)
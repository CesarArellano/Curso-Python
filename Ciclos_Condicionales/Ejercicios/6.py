"""
* @file 6.py
*
* @brief Remplazar cada letra de una frase dada por el usuario por la
* posición que le corresponde en el abecedario y mostrar el nuevo string
* en pantalla (Los espacios no se remplazan).
* Ejemplo: frase : 'Hola' salida : 815121 H(8) o(16) l(12) a(1)
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

abecedario="abcdefghijklmnñopqrstuvwxyz"
nueva_frase = ""
letras = ""
frase = input("Ingrese la frase\n")

for letra in frase:
	nueva = letra.lower()
	for i in range(27):
		if nueva == abecedario[i]:
			nueva_frase += str(i+1)
			letras += " " + letra + "(" + str(i+1) + ")"
nueva_frase += letras

print("Salida:",nueva_frase)
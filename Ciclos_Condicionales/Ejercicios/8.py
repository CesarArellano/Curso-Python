"""
* @file 8.py
*
* @brief Mostrar en pantalla la frecuencia de aparición de vocales
* en una frase dada por el usuario.
* Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1
* 
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

vocales = "aeiou"
frase = input("Ingrese la frase\n")

print("Salida:")
for i in range(5):
	cantv = 0
	for letra in frase:
		nueva_letra = letra.lower()
		if nueva_letra == vocales[i]:
			cantv += 1
	if cantv !=0:
		print(vocales[i],"=",cantv," ")
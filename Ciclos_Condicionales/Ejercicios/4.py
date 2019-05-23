"""
* @file 4.py
*
* @brief Dada una lista de frases ingresadas por el usuario,
* mostrar en pantalla todas aquellas que sean palíndromo.
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

palindromos = []
frases = ""

while frases != 'S' and frases !='s':
	frases = input("Ingresa la frase, (S, s) para terminar.\n")
	if frases != 'S' and frases != 's':
		palindromos.append(frases)

for i in range(0,len(palindromos)):
	frase = palindromos[i]
	frase = frase[::-1]
	frase = frase.replace(" ","")
	frase = frase.lower()
	frase2 = palindromos[i].replace(" ","")
	frase2 = frase2.lower()
	if frase == frase2:
		print("La frase: %s"%(palindromos[i]),"es un palindromo")
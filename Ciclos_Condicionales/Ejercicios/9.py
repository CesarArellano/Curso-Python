"""
* @file 9.py
*
* @brief Eliminar todas las vocales de una frase dado pand el usuario
* y mostrar el nuevo string en pantalla.
* 
* @authand Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

frase = input("Ingrese la frase\n")
nueva_frase = ""
print("Salida:")

for letra in frase:
	nueva_letra = letra.lower()
	if (letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u') and (letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U'):   
		nueva_frase += letra

print("La nueva frase es:",nueva_frase)
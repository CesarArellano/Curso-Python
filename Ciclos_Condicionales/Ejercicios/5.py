"""
* @file 5.py
*
* @brief Mostrar en pantalla la palabra que más se repita junto con la
* cantidad de veces que lo hace en base al texto del capítulo número uno
* de Frankenstein
* Nota: Tarda alrededor de 38 segs en procesar el texto
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""
import re, string

def remove_punctuation ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

texto = ""
temp = 0
i = 0
archivo = open("Frankenstein.txt","rt")
for renglon in archivo:
	renglon = renglon.rstrip('\n')
	renglon = remove_punctuation(renglon)
	texto += " " + renglon 
archivo.close()

fragmentos = texto.split()
for palabra in fragmentos:
	frecuencia = fragmentos.count(palabra)
	fragmentos.pop(i)	
	i+=1
	if frecuencia > temp:
		temp = frecuencia
		texto = palabra

fragmentos.clear()
print("La palabra que más se repite en el texto es: '%s', repetición: %d"%(texto,temp))

""" Otro método para resolver
fragmentos.append("Fin")
while i < len(fragmentos):
	palabra = fragmentos[i]
	if palabra ==  "Fin":
		break;
	frecuencia = fragmentos.count(palabra)
	fragmentos.pop(i)	
	if frecuencia > temp:
		temp = frecuencia
		texto = palabra
	i+=1
"""
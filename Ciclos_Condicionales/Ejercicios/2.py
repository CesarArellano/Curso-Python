"""
* @file 2.py
*
* @brief A partir del diccionario del ejercicio anterior (1.py,
* mostrar en pantalla la materia con mejor promedio.
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

calificaciones = {"Cálculo":9.6, "Álgebra Lineal":9.1, "Física 2": 8.7, "Programación Aplicada": 10}
temp = 0
for calificacion in calificaciones.items():
	if calificacion[1] > temp:
		temp = calificacion[1]
		materia = calificacion[0]

print("La materia con mejor promedio es:", materia)


"""
* @file 1.py
*
* @brief Dado un diccionario, el cual almacena las calificaciones de un alumno,
* siendo las llaves los nombres de las materia y los valores las calificación,
* mostrar en pantalla el promedio del alumno.
*
* @author Arellano Velásquez Cesar Mauricio
*
* @date 22/05/2019
"""

calificaciones = {"Cálculo":9.6, "Álgebra Lineal":9.1, "Física 2": 8.7, "Programación Aplicada": 10}
promedio = 0
contador = 0
for calificacion in calificaciones.values():
	promedio += calificacion 
	contador += 1

promedio /= contador
print("El promedio es:", promedio)


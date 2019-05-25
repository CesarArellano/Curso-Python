def saludo(nombre : str) -> None: # Indica el tipo de variables en los parametros y que la función no retorna ningún valor
	print("Hola " + nombre)

def suma(num1 : int, num2 : int = 100) -> int:  # Las anotaciones no afectan a la hora de interpretar o compilar, ya que puede recibir cualquier parametros a pesar de que en las anotaciones indique lo contrario.
	return num1 + num2

nombre = "Cesar"
saludo(nombre)

print(suma(10))

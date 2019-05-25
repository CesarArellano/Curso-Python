"""
from calculadora import *
from calculadora import (suma,
						resta,
						division)
from calculadora import suma as nueva_suma
print(suma(10,20))
print(resta(10,20))
print(division(10,20))
"""
import calculadora # Esto es un módulo

print(calculadora.__name__)
print(__name__) # Imprime __main__

lenguajes = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"
copia = lenguajes
resultado = lenguajes.split("; ") # Resultado es una lista

nuevo_string = " ".join(resultado)

texto = """Esto es un texto
con 
saltos
de

linea"""

resultado =texto.splitlines()

print(resultado)
print(nuevo_string)
print(copia)

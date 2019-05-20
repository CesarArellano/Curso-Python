curso = "Python"
version = "3"

#resultado = "Curso de %s %s" %(curso,version)
resultado = "Curso de {a} {b}".format(a=curso,b=version)

print(resultado)
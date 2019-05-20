tupla = (1,2,3,4,5)
lista = [10,20,30,40,50]

resultado = zip(tupla,lista)
#resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)

"""
uno,dos,tres,cuatro,cinco = tupla
print(uno,dos,tres,cuatro,cinco)

uno,*dos,cinco = tupla
print(uno,dos,cinco)
"""

import time
dia_actual = int(time.strftime("%d"))
mes_actual = int(time.strftime("%m"))
anio_actual = int(time.strftime("%Y"))

dia = int(input("Ingresa el dia de nacimiento\n"))
mes = int(input("Ingresa el mes de nacimiento\n"))
anio = int(input("Ingresa el año de nacimiento\n"))

aux = (anio*365)+(mes*30)+dia
aux2 = (anio_actual*365)+(mes_actual*30)+dia_actual 
dias_trans = aux2-aux
mes_trans = dias_trans*0.0329
print("Meses transcurridos:",mes_trans)
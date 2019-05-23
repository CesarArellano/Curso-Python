diccionario = {"a":1, "b":2, "c":3, "a": 4}
resultado = diccionario["a"] #Obtener valor de la llave "a"
resultado = "z" in diccionario #Indica True o False dependiendo si está en el diccionario
resultado = diccionario.get("z", {}) #Retorna el valor, sino existe retorna el segundo parámetro
resultado = diccionario.setdefault("z",3)
print(resultado)
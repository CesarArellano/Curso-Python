mensaje = "Hola yo soy 'César'"

resultado = mensaje.count("Cesar") # Cuantas veces aparece Cesar en el string
resultado = "Cesar" in mensaje # Se encuentra en el string
resultado = mensaje.find("César") # En que posición del arreglo aparece Cesar en la frase
resultado = mensaje[resultado: resultado +len("Cesar")] #Imprime desde comienza hasta donde termina Cesar
resultado = mensaje.startswith("H") # Retorna False o True si es que la letra o palabra esta al inicio del arreglo
print(resultado)
print(mensaje)
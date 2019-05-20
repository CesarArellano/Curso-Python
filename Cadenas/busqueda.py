mensaje = "Hola yo soy 'César'"

resultado = mensaje.count("Cesar")
resultado = "Cesar" in mensaje
resultado = mensaje.find("César")
resultado = mensaje[resultado: resultado +len("Cesar")]
resultado = mensaje.startswith("H")
print(resultado)
print(mensaje)
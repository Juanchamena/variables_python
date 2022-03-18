# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

print(nombre, apellido)

# Almacenar su nombre completo en una variable
# nombre_completo = .....

nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)

letras_nombre = len(nombre)
letras_apellido = len(apellido)
cantidad_letras = letras_nombre + letras_apellido
print(cantidad_letras) 

#O bien, también podria hacerlo de la siguiente manera, para restar el espacio ya que lo cuenta como caracter.

cantidad_letras2= len(nombre_completo) - 1
print(cantidad_letras2)


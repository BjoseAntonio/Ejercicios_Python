# # Ejercicio 1
# # Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

# nombreUsuario = input("Introduce tu nombre: ")
# numero = int(input("Introduce un numero: "))
# print((nombreUsuario+"\n")*numero)



# # Ejercicio 2
# # Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# nombreCompleto = input("Ingresa tu nombre completo: ")
# print(nombreCompleto.lower())
# print(nombreCompleto.upper())
# print(nombreCompleto.title()) 



# # Ejercicio 3
# # Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

# nombreUser = input("Introduce tu nombre: ")
# cantidadLetra = len(nombreUser)
# print("El nombre introduccido es '"+nombreUser.upper()+"', con una cantidad de '"+str(cantidadLetra)+"' palabras.")



# # Ejercicio 4
# # Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
# numTelefono = input("Introduce tu numero de telefono(Formato: +34-913724710-56): ")
# print("el numero introduccio es: "+numTelefono[4:-3])

# # Ejercicio 5
# # Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
# frase = input("Introduce una frase: ")
# fraseInvertida = frase[::-1]
# print(fraseInvertida)

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

oracion = input("Introduce una frase: ")
vocal = input("Introduce un vocal: ")

# sel_vocal_oracion = 

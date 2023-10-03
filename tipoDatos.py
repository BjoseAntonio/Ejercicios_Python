# "TIPOS DE DATOS SIMPLRES"
# Link: https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
#1 # Escribir un programa que muestre en pantalla 'Hola mundo' 
# print('Hola mundo')

# 2# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
# cadena = '¡Hola mundo!'
# print(cadena)

# 3# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
# nombreUsuario = input('Nombre: ')
# print('¡Hola '+nombreUsuario+'!')

#4 # Ejercicio 4
# # Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# total_Suma = 3+2
# total_Division = total_Suma / 2.5
# totalOperacion = total_Division**2
# print(str(totalOperacion))

# # Ejercicio 5
# # Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
# costoPorHora = 230
# horasTrabajo = int(input('Numero de horas trabajadas: '))
# pagaPorHora = costoPorHora * horasTrabajo
# print('Factura de pago por horas elaboradas: $'+str(pagaPorHora))


# # Ejercicio 6
# # Escribir un programa que lea un entero positivo, 
# # , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# # . La suma de los 
# #  primeros enteros positivos puede ser calculada de la siguiente forma:

# # indice =  1
# # suma = 0
# # caja = 0
# numero = int(input("ingresa un numero: ")) 
# # while indice <= numero:
#     # print(str(indice)+" : "+str(numero))
#     # caja  += indice
#     # # caja += caja
#     # indice += 1 
# suma= (numero *( numero + 1 )) / 2
# print("La suma de los numero del 1 al "+str(numero)+" es: "+ str(suma))




# # Ejercicio 7
# # Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> do
# nde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# peso = int(input("Cual es tu peso?(en KG): "))
# estatura_CM = float(input("Cual es tu estatura?(En CM): "))
# estatura_Metros = estatura_CM / 100
# imc = peso / (estatura_Metros**2)
# print("Tun índice de masa corporal es "+str(imc))


# # Ejercicio 8
# # Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# dividendo = int(input("Introduce un numero: ")) 
# divisor = int(input("Introduce un segundo numero: ")) 
# cociente = dividendo / divisor
# resto = dividendo % divisor
# print("El resultado de la division es: "+str(round(cociente))+" y su resto es: "+str(round(resto)))



# # Ejercicio 9
# # Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# inversion = int(input("Dinero a invertir: "))
# interes_anual = int(input("Interes porcentual anual: "))
# anual = int(input("años: "))
# capital =round(inversion*(interes_anual / 100 + 1)**anual,2)
# print(capital)



# # Ejercicio 10
# # Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

# peso_Payaso = 112
# peso_muñeca = 75
# pedido_Muñecas = input("Ventas de muñecas del ultimo pedido: ")
# pedido_Payasos = input("Ventas de payasos del ultimo pedido: ")
# peso_pedido = (int(pedido_Muñecas)*peso_muñeca) + (int(pedido_Payasos)*peso_Payaso)
# print("Las muñecas vendidas son '"+str(pedido_Muñecas)+"' y de payasos es '"+str(pedido_Payasos)+"', donde el peso del envio es: "+str(peso_pedido)+"g")



# # Ejercicio 11
# # Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
# cuenta_ahorro = float(input("Introduce la cantidad de ahorro: "))

# interes = 0.04
# ahorros1 = cuenta_ahorro *(1 +interes)
# print("primer año: "+str(round(ahorros1, 2)))
# ahorros2 = ahorros1*(1+ interes)
# print("Segundo año: "+str(round(ahorros2, 2)))
# ahorros3 = ahorros2*(1+ interes)
# print("Tercer año: "+str(round(ahorros3, 2)))



# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precio = 3.49
Descuento = 60
cantidad_panConDescuento = float(input("Introduce las barras de pan vendidas que no son del dia: "))
precioPorDescuento = (precio * Descuento) / 100
costo_final = cantidad_panConDescuento * precioPorDescuento
print("Precio normal de barra de pan: "+str(precio)+("€"))
print("Descuento del '60%'por pan no del dia con un precio de: "+str(precioPorDescuento)+("€"))
print("Costo final: "+str(costo_final)+("€"))
#Actividades

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#edad = int (input("Ingrese su edad "))
#if edad > 18:
#    print ("Es mayor de edad")
#else:
#    print ("Es menor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#nota = float (input ("Ingrese su nota "))
#if nota >= 6:
#    print ("Aprobado")
#else:
#    print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#numero = int (input("Ingrese un numero "))
#if numero % 2 == 0:
#    print ("El numero es Par")
#else:
#    print ("El numero es Impar")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años

#edad = int (input("Ingrese su edad "))
#if edad < 12:
#    print ("menor de 12 años")
#elif (edad <= 12 and edad<18):
#    print ("Es Adolecente")
#elif (edad>=18 and edad <30):
#    print ("Adulto/a joven")
#else (edad >=30):
#    print ("Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.



#contrasena = str (input("Introducir contraseña "))
#longitud = len(contrasena)
#if (longitud >=8 and longitud <=14):
#    print ("Ha ingresado una contraseña correcta")
#else:
#    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

#import random
#from statistics import mode, median, mean

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#moda = mode(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#media = mean(numeros_aleatorios)

#if media > mediana and mediana > moda:
#    sesgo = "positivo o a la derecha"
#elif media < mediana and mediana < moda:
#    sesgo = "negativo o a la izquierda"
#else:
#    sesgo = "sin sesgo"

#print(f"La lista de números aleatorios es: {numeros_aleatorios}")
#print(f"Moda: {moda}")
#print(f"Mediana: {mediana}")
#print(f"Media: {media}")
#print(f"La distribución tiene un sesgo {sesgo}.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

#frase = str (input("Ingrese una frase o palabra "))
#ultima_letra = frase[-1]
#voc = (f"a")
#voc1 = (f"e")
#voc2 = (f"i")
#voc3 = (f"o")
#voc4 = (f"u")

#if (ultima_letra == voc):
#    print ((frase) , "!")
#elif (ultima_letra == voc1):
#    print ((frase) , "!")
#elif (ultima_letra == voc2):
#    print ((frase) , "!")
#elif (ultima_letra == voc3):
#    print ((frase) , "!")
#elif (ultima_letra == voc4):
#    print ((frase) , "!")

#else:
#    print (frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.#

#nombre = str (input("Ingrese su nombre "))

#opcion = int (input("Ingrese 1 si quiere su nombre en mayúsculas\n"
#                    "Ingrese 2 si quiere su nombre en minúsculas\n"
#                    "Ingrese 3 si quiere su nombre con la primera letra mayúscula\n"))

#if (opcion == 1):
#    print (nombre.upper())

#elif (opcion == 2):
#    print (nombre.lower())

#elif (opcion == 3):
#    print (nombre.title())

#else:
#    pass
    

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#magnitud = float (input("Ingrese la magnitud de un terremoto "))

#if (magnitud < 3):
#    print ("Muy leve")

#elif (magnitud <= 3 and magnitud<4):
#    print ("Leve")

#elif (magnitud <= 4 and magnitud<5):
#    print ("Moderado")

#elif (magnitud <= 5 and magnitud<6):
#    print ("Fuerte")

#elif (magnitud <= 6 and magnitud<7):
#    print ("Muy Fuerte")

#elif (magnitud >=7):
#    print ("Extremo")

#else:
#   pass

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año
#Estación en el
#hemisferio norte
#Estación en el
#hemisferio sur
#Desde el 21 de diciembre hasta el 20 de
#marzo (incluidos)
#Invierno Verano
#Desde el 21 de marzo hasta el 20 de junio
#(incluidos)
#Primavera Otoño
#Desde el 21 de junio hasta el 20 de
#septiembre (incluidos)
#Verano Invierno
#Desde el 21 de septiembre hasta el 20 de
#diciembre (incluidos)
#Otoño Primavera

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()   #en que hemisferio estoy y lo pasa a mayuscula
#mes = input("¿Qué mes del año es?: ").capitalize()   #primera letra del mes en mayuscula
#dia = int(input("¿Qué día del mes es?: "))

#estacion = ""     #cargo variable

#if hemisferio == 'N':         #primera comparacion
#    if (mes == "Diciembre" and dia >= 21) or (mes == "Enero") or (mes == "Febrero") or (mes == "Marzo" and dia <= 20):
#        estacion = "Invierno"
#    elif (mes == "Marzo" and dia >= 21) or (mes == "Abril") or (mes == "Mayo") or (mes == "Junio" and dia <= 20):
#        estacion = "Primavera"
#    elif (mes == "Junio" and dia >= 21) or (mes == "Julio") or (mes == "Agosto") or (mes == "Septiembre" and dia <= 20):
#        estacion = "Verano"
#    elif (mes == "Septiembre" and dia >= 21) or (mes == "Octubre") or (mes == "Noviembre") or (mes == "Diciembre" and dia <= 20):
#        estacion = "Otoño"
#elif hemisferio == 'S':      #sino fue hemisferio N es S sino Hemisferio no valido
#    if (mes == "Diciembre" and dia >= 21) or (mes == "Enero") or (mes == "Febrero") or (mes == "Marzo" and dia <= 20):
#        estacion = "Verano"
#    elif (mes == "Marzo" and dia >= 21) or (mes == "Abril") or (mes == "Mayo") or (mes == "Junio" and dia <= 20):
#        estacion = "Otoño"
#    elif (mes == "Junio" and dia >= 21) or (mes == "Julio") or (mes == "Agosto") or (mes == "Septiembre" and dia <= 20):
#        estacion = "Invierno"
#    elif (mes == "Septiembre" and dia >= 21) or (mes == "Octubre") or (mes == "Noviembre") or (mes == "Diciembre" and dia <= 20):
#        estacion = "Primavera"
#else:
#    estacion = "Hemisferio no válido."    #por si escribo algun dato de forma incorrecta

#print(f"Usted se encuentra en: {estacion}")
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”...

#print ("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
#nombre = input ("Hola, como te llamas?")
#print (f"Hola", nombre)


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

#nombre = input ("Ingrese su nombre ")
#apellido = input ("Ingrese su apellido ")
#edad = int(input ("Ingrese su edad "))
#lugar = input ("Lugar de residencia ")
#print (f"Soy ", nombre , apellido, ", tengo ", edad , " y vivo en ", lugar)

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

#import math
#pi_value = math.pi

#radio = int (input ("Ingrese el radio del circulo ")) 
#area = pi_value * radio**2
#perimetro = 2*pi_value*radio

#print (f"El area es ", area)
#print (f"El perimetro es de ", perimetro)

#pi = 3.14
#radio = int (input ("Ingrese el radio del circulo ")) 
#area = pi * (radio**2)
#perimetro = 2*pi*radio

#print (f"El area es ", area)
#print (f"El perimetro es de ", perimetro)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

#equivhs = int(input ("Ingrese segundos para su equivalente en hs "))
#print (f"El equivalente es ", equivhs/60 , "horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

#num_tabla = int(input ("Ingrese un numero para hacer su tabla de multiplicar "))
#print (f"1 x", num_tabla, "=", num_tabla*1)
#print (f"2 x", num_tabla, "=", num_tabla*2)
#print (f"3 x", num_tabla, "=", num_tabla*3)
#print (f"4 x", num_tabla, "=", num_tabla*4)
#print (f"5 x", num_tabla, "=", num_tabla*5)
#print (f"6 x", num_tabla, "=", num_tabla*6)
#print (f"7 x", num_tabla, "=", num_tabla*7)
#print (f"8 x", num_tabla, "=", num_tabla*8)
#print (f"9 x", num_tabla, "=", num_tabla*9)
#print (f"10 x", num_tabla, "=", num_tabla*10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#num1 = int(input ("Ingrese numero distinto de cero "))
# no funcionan los if tengo q corregirlo
# if num1 > 0 
#print (f"Ingrese nuevamente el numero mayor a cero ",)
#num2 = int(input ("Ingrese numero distinto a cero "))
#if num2 < 0  print("Ingrese nuevamente el numero mayor a cero ")
#print (f"La suma de los numeros es de " , num1+num2)
#print (f"La division es de " , num1/num2)
#print (f"La multiplicacion es de " , num1*num2)
#print (f"La resta es de " , num1-num2)


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = (𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 *(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚))/2
#2

#peso = float(input ("Ingrese su peso en kg "))
#altura = float(input ("Ingrese su altura en mts "))
#print (f"Su Imc es " , peso/(altura**2))

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

#gradosF = float(input ("Ingrese temperatura en grados Celsius "))
#constante = 32
#print (f"El equivalente en grados Fahrenheit es " , ((gradosF-constante)*(5/9)))

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números

#mun1 = float (input("ingrese numero 1 "))
#mun2 = float (input("ingrese numero 2 "))
#mun3 = float (input("ingrese numero 3 "))

#print (f"El promedio de los 3 numeros es " , ((mun1+mun2+mun3)/3)  )

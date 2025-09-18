#Actividades:

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for num in range (0,101 ):     # cuenta desde 0 a 100 inclusive
#    print (num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#num = int(input("Ingrese un numero entero "))            #solicita el ingreso de un numero entero
#cant_digitos = len(str(num))                             # len devuelve la logitud de num 
#print (f"El numero tiene" , (cant_digitos) , "digitos")   #imprime por pantalla cantidad de digitos

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#num1 = int(input("Ingrese un numero entero "))  #ingreso de datos
#num2 = int(input("Ingrese un segundo numero entero menor al num1 "))  #ingreso de datos

#suma = 0                                      # cargo variable con valor cero
        
#for numero_actual in range(num2 + 1, num1): 
#    suma += numero_actual                  #suma los numeros internos excluyendo los extremos

#print(f"La suma de todos los numeros es: {suma}") #imprime en pantalla el resultado


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

# Inicializar la variable para la suma
#suma_total = 0

# Bucle para solicitar números al usuario
#while True:
#    try:
#        # Solicitar al usuario que ingrese un número entero
#        numero = int(input("Ingrese un número entero (o 0 para terminar): "))
#
#        # Si el número ingresado es 0, detener el bucle
#        if numero == 0:
#            break
#        else:
#            # Sumar el número a la suma total
#            suma_total += numero
#    except ValueError:
#        # Manejar el caso en que el usuario ingrese algo que no es un número entero
#        print("Entrada no válida. Por favor, ingrese un número entero.")

# Mostrar el total acumulado
#print(f"\nEl total acumulado de los números ingresados es: {suma_total}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#import random   #biblioteca numeros aleaorios

#numero_aleatorio = random.randint(0, 9)  # Genera un número entre 0 y 9 (inclusive)
#intentos = 0


#print("Ingrese un numero de  0 y 9.")

# 2. Bucle de juego
#while True:
#    try:
#        numero_usuario_str = input("Introducir numero: ")
#        numero_usuario = int(numero_usuario_str)
#        intentos += 1 # Aumenta el contador de intentos

        
#        if numero_usuario == numero_aleatorio:   #compara si el numero ingresa es igual al aleatorio
#            print(f"Adivinaste el número en {intentos} intentos.")
#            break  # Sale del bucle si se acertó
#        elif numero_usuario < numero_aleatorio:
#            print("El número que busco es mayor.")
#        else: # numero_usuario > numero_aleatorio
#            print("El número que busco es menor.")

#    except ValueError:
#        print("Por favor, introduce un número válido (0-9).")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#for i in range(100, -1, -2):   # limite del rango, invierte el orden y solo los numeros pares
#    print(i, end=", ")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#while True:
#    try:
#        numero_ingresado = int(input("Ingresar un número entero positivo: "))  #ingresar un numero entero positivo
#        if numero_ingresado >= 0:
#            break  # Salir del bucle si el número es válido
#        else:
#            print("Ingresar un número entero no negativo.")
#    except ValueError:
#        print("Valor no valido, ingresar un número entero.")


#suma_total = sum(range(numero_ingresado + 1)) #suma de todos los numeros hasta el numero ingresado

#print(f"La suma de todos los números desde 0 hasta {numero_ingresado} es: {suma_total}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#cantidad_numeros = 100   #numeros a ingresar

#pares_count = 0
#impares_count = 0
#positivos_count = 0
#negativos_count = 0

#for i in range(cantidad_numeros):    #ingreso de numeros
#    while True:
#        try:
#            numero = int(input(f"Ingrese el número {i + 1}: "))
#            break
#        except ValueError:
#            print("Entrada inválida. Por favor, ingrese un número entero.")
#
#    
#    if numero % 2 == 0:      #para saber si es par o imprar
#        pares_count += 1
#    else:
#        impares_count += 1
#
##    if numero > 0:
#        positivos_count += 1
#    elif numero < 0:
#        negativos_count += 1


#print(f"\nResultados:")
#print(f"Cantidad de números pares: {pares_count}")
#print(f"Cantidad de números impares: {impares_count}")
#print(f"Cantidad de números positivos: {positivos_count}")
#print(f"Cantidad de números negativos: {negativos_count}")



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#numeros = []   #inicializo lista vacia

#print("Por favor, ingresa 100 números enteros:")  #Ingreso 100 numeros
#for i in range(100):
#    while True:
#        try:
#            num_str = input(f"Ingresa el número #{i + 1}: ")
#            num = int(num_str)
#            numeros.append(num) # Agrega el número a la lista
#            break # Sale del bucle de reintento si la entrada es válida
#        except ValueError:
#            print("Entrada no válida. Por favor, ingresa un número entero.")


#suma_total = sum(numeros) #suma total de la lista

#cantidad_numeros = len(numeros)  #suma de la cantidad de numeros por si cambio y no es 100

#media = suma_total / cantidad_numeros   #calculo promedio

#print(f"\nLa suma de los 100 números es: {suma_total}")  #valores en pantalla
#print(f"La media de los 100 números es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#def invertir_digitos(numero_str):
  
#  return numero_str[::-1] 

# Solicitar el número al usuario
#numero_ingresado = input("Ingresa un número: ")

# Invertir los dígitos
#numero_invertido_str = invertir_digitos(numero_ingresado)

#print("Número invertido:", int(numero_invertido_str))
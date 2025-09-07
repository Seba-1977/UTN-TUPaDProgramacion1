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

num1 = int(input("Ingrese un numero entero "))  #ingreso de datos
num2 = int(input("Ingrese un segundo numero entero menor al num1 "))  #ingreso de datos

suma = 0                                      # cargo variable con valor cero
        
for numero_actual in range(num2 + 1, num1): 
    suma += numero_actual                  #suma los numeros internos excluyendo los extremos

print(f"La suma de todos los numeros es: {suma}") #imprime en pantalla el resultado


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.




#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.



#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.



#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.




#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).





#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).



#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
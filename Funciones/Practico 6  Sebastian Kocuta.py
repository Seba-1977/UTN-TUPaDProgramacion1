#Práctico 2: Funciones en Python

#Objetivo:
#Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos que implementen modularidad, reutilización de código y
#una organización estructurada para resolver problemas.
#Resultados de aprendizaje:
#Fundamentos de las Funciones: A través de explicaciones teóricas y
#ejercicios prácticos, el estudiante desarrollará habilidades para definir, llamar y reutilizar funciones en Python.
#Modularidad y Reutilización: El estudiante será capaz de descomponer
#problemas complejos en pequeñas unidades funcionales, mejorando la claridad, mantenimiento y reutilización del código.
#Resolución de Problemas con Funciones: El estudiante aplicará funciones para resolver problemas computacionales que involucren cálculos matemáticos, manipulación de datos y flujos de control más complejos.
#Buenas Prácticas: El estudiante aprenderá a estructurar el código usando funciones y a documentar adecuadamente cada una para facilitar su
#comprensión.

#Actividades:

#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#Definicion de Funciones
#def imprimir_hola_mundo():
#    print("Hola mundo!")

#Programa Principal
#imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#Definicion de Funciones

#def saludar_usuario(nombre):
#    print(f"Hola {nombre}!")

#Programa Principal

#saludar_usuario("Marcos")

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definicion de Funciones
#def informacion_personal(nombre, apellido, edad, residencia):
#    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal
#informacion_personal("Sebastian", "Kocuta", "48", "Anisacate")


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
# radio al usuario y llamar ambas funciones para mostrar los resultados.


#Definicion de Funciones

#pi=3.14
#def calcular_area_circulo(radio):
#    return (pi *  radio * 2)
    
#def calcular_perimetro_circulo(radio):
#    return pi * radio  **2

#Programa Principal

#radio =float(input(f"ingrese el radio para calcular su area  y su perimetro: "))

#print(f"El area del circulo es de {calcular_area_circulo (radio):.2f} y su perimetro {calcular_perimetro_circulo (radio):.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


#Definicion de Funciones
#def segundos_a_horas(segundos):
#    return segundos / 3600

#Programa Principal

#segundos = float(input("Ingresa cantidad de segundos para saber a cuantas horas equivale:  "))

#horas=segundos_a_horas(segundos)

#print(f"Los {segundos} segundos equivalen a {horas:.2f} horas")


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.


#Definicion de Funciones
#def tabla_multiplicar(numero):
#    for i in range(1, 11):
#        resultado = numero * i
#        print(f"{numero} x {i} = {resultado}")

#Programa Principal

#numero = int(input(f"Ingrese un numero para obtener su tabla de multiplicar:  "))

#tabla = tabla_multiplicar(numero)

#print(tabla)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#Definicion de Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion =  a * b
    if (b!=0):
        division = a/b
    else:
        division = print("No se puede dividir por cero ")

    return (suma, resta, multiplicacion, division)

#Programa Principal

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero:  "))

resultados = operaciones_basicas(num1, num2)

print(f"Los números ingresados son: {num1} y {num2}")
print(f"Resultado de la suma: {resultados[0]}")
print(f"Resultado de la resta: {resultados[1]}")
print(f"Resultado de la multiplicación: {resultados[2]}")
print(f"Resultado de la división: {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.



#Definicion de Funciones


#Programa Principal


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.



#Definicion de Funciones


#Programa Principal



#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.


#Definicion de Funciones


#Programa Principal


#Consejo:
#Antes de empezar, analiza cada problema y piensa cómo dividirlo en
#pasos más pequeños utilizando funciones.
#Al terminar, prueba cada función con diferentes entradas para verificar
#que funciona correctamente.

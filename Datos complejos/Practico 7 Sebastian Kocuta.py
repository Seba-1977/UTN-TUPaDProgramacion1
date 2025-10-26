
#Práctico 7: Estructuras de datos complejas
#Objetivo:

#Dominar el uso de estructuras de datos complejas en Python para
#almacenar, organizar y manipular datos de manera eficiente, aplicando
#buenas prácticas y optimizando el rendimiento de las aplicaciones.
#Resultados de aprendizaje:
#1. Comprensión y aplicación de iterables: listas, tuplas y sets.
#2. Introducción a estructuras de datos complejas: diccionarios.
#Actividades

#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300


#diccionario_precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#diccionario_precios_frutas["naranjas"]=1200
#diccionario_precios_frutas["Manzanas"]=1500
#diccionario_precios_frutas["Peras"]=2300

#print (diccionario_precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

#diccionario_precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#diccionario_precios_frutas["naranjas"]=1200
#diccionario_precios_frutas["Manzanas"]=1700
#diccionario_precios_frutas["Peras"]=2300
#diccionario_precios_frutas["Melón"]=2800

#print (diccionario_precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

#diccionario_precios_frutas = {'Peras', 'Melón', 'Manzanas', 'Uva', 'Naranja', 'Ananá', 'Banana'}

#print (diccionario_precios_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#agenda = {}

#for i in range(5):
#    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
#    numero = input(f"Ingrese el número telefónico de {nombre}: ")
#    
#    agenda[nombre] = numero

#print("\nAgenda cargada correctamente")
#print("Contactos guardados:")
#print(agenda) 

#consulta = input("\nIngresá el nombre del contacto que querés consultar: ")

#if consulta in agenda:
#    print(f"El número de {consulta} es: {agenda[consulta]}")
#else:
#    print(f"No se encontró ningún contacto con el nombre '{consulta}'.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.


#frase = input("Ingrese una frase: ")

#palabras = frase.split()

#palabras_unicas = set(palabras)

#conteo_palabras = {}
#for palabra in palabras:
#    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

#print("\nPalabras únicas:")
#print(palabras_unicas)

#print("\nConteo de palabras:")
#print(conteo_palabras)


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

#alumnos = {}

#for i in range(3):
#    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
#    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
#    
#    alumnos[nombre] = notas

#print("\nPromedios de los alumnos:")
#for nombre, notas in alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"{nombre}: {promedio:.2f}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#parcial1 = {1, 2, 3, 4, 5}
#parcial2 = {4, 5, 6, 7}

#ambos = parcial1 & parcial2

#solo_uno = parcial1 ^ parcial2

#al_menos_uno = parcial1 | parcial2

#print("Aprobaron ambos parciales:", ambos)
#print("Aprobaron solo uno de los dos:", solo_uno)
#print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

#3stock = {
#    "manzanas": 10,
#    "bananas": 5,
#    "naranjas": 8
#}

#print("Stock inicial:", stock)

#producto = input("\nIngrese el nombre del producto: ").lower()

#if producto in stock:
#    print(f"El producto '{producto}' tiene {stock[producto]} unidades en stock.")
#    
#    
#    agregar = input("¿Desea agregar unidades? (s/n): ").lower()
#    if agregar == "s":
#        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
#        stock[producto] += cantidad
#        print(f"Stock actualizado de '{producto}': {stock[producto]} unidades.")
#    else:
#        print("No se realizaron cambios en el stock.")
#else:
#    print(f"El producto '{producto}' no existe en el inventario.")
    
#    agregar_nuevo = input("¿Desea agregarlo? (s/n): ").lower()
#    if agregar_nuevo == "s":
#        cantidad = int(input("Ingrese la cantidad inicial en stock: "))
#        stock[producto] = cantidad
#        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
#    else:
#        print("No se agregó el producto.")

#print("\nStock final:", stock)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.




#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

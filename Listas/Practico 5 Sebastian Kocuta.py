#Actividades:
#NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.

#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

#Crear la lista de notas
#notas =[7, 9, 5, 4, 9, 7, 4, 6, 6, 8]

#mostrar la lista
#print ("Notas:")
#for n in notas:
#    print (n, end=", ")   #imprime notas separadas por espacio y coma ,
#print()

#Calculo de promedio y se muestra

#promedio = sum(notas) / len (notas)
#print ("Promedio:", promedio)

#Indica nota minima y maxima
#print ("Nota mas alta", max(notas))    #Busca el maximo en la lista
#print ("Nota mas baja:", min(notas))   #Busca el minimo en la lista


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#productos = []               #Ingresar 5 productos
#for i in range (5):
#    item = input (f"Ingrese el produco {i+1}: ")
#    productos.append (item)

#print("\nLista original de productos: ")  #se imprime la lista con los 5 productos
#print(productos)

#print("\Lista ordenada alfabeticamente: ")
#print(sorted(productos))      #funcion sorted ordena alfabeticamente la lista de productos

#eliminar = input ("\nIngrese el producto que desea eliminar ")   #Se solicita que producto desea eliminar
#if eliminar in productos:
#    productos.remove(eliminar)
#    print (f"\n`{eliminar}` fue eliminado de la lista")
#else:                                                            #si el producto no esta en la lista
#    print (f"\nEl productos `{eliminar}` no  esta en la lista")

#print("\nLista actualizada: ")
#print (productos)                  #Imprime la lista actualizada


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

#import random   #libreria que genera numeros al azar

#numeros = []   #Se crea una lista vacia para guardar los 15 numeros

#for i in range (15):       #Se repite 15 veces el bucle for para buscar 15 numeros aleatorios
#    numero_aleatorio = random.randint (1,100)
#    numeros.append (numero_aleatorio)
#print ("Lista origina: ", numeros)

#pares = []    #Se crea la lista pares
#impares = []   #Se crea la lista impares

#for numero in numeros:
#    if numero % 2==0:                   #busca los numeros pares
#        pares.append(numero)
#    else:                               #Sino son numeros pares va a ser impares
#        impares.append(numero)

#print ("Lista de numeros pares: ", pares)             #Muestra la lista de numeros pares
#print ("Cantidad de numeros pares: ", len(pares))    #cuenta los numeros y muestra la cantidad

#print ("Lista de numeros impares: ", impares)           #Muestra la lista de numeros impares
#print ("Cantidad de numeros impares: ", len(impares))  #cuenta la cantidad de numeros impares y los muestra por pantalla


#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
#Datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

#datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#sin_duplicados = []   #Se crea lista vacia

#for d in datos:
#    if d not in sin_duplicados:      #busca datos no duplicados
#        sin_duplicados.append(d)     #si esta duplicado no lo agrega

#print ("Lista original: ")          #mostrar lista original
#for d in datos:                     
#    print (d, end=", ")              #imprime los numeros por separados con ,
#print ()

#print ("Lista sin duplicados: ")
#for d in sin_duplicados:              
#    print(d, end=", ")              #imprime los numeros por separados con ,
#print()


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

#asistencia =["Sebastian" ,"Jeronimo" ,"Emiliano" , "Juan" , "Pedro" , "Jorge" , "Raul" , "Rodolfo"]

#print("Asistencia actual: ")
#for a in asistencia:                #recorre la lista de asistencia
#    print(a)

#opcion = input("Desea agregar (A) o eliminar (E) un estudiante: ").upper()

#if opcion == "A":                                     #Agrego un nuevo asistente
#    nuevo = input("Ingrese el nombre a agregar: ")
#    asistencia.append(nuevo)

#elif opcion == "E":                                  #Elimino un aistente
#    eliminar=input("Ingrese el nombre a eliminar: ")
#    if eliminar in asistencia:
#        asistencia.remove(eliminar)
#    else:
#        print ("Ese estudiante no esta en la lista")

#print("Lista final de asistentes: ")             #imprime la lista definitaba con el agregado o eliminacion de asistente
#for a in asistencia:
#    print(a)

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

#numeros =[1,2,3,4,5,6,7]    #lista con 7 numeros

#ultimo = numeros[-1]     #el ultimo numero pasa a ser el primero
#resto = numeros[:-1]     #coloco todos los numeros menos el ultimo  
#lista_rotada = [ultimo] + resto      #armo la lista con el 7 primero y luego el resto

#print(lista_rotada)     #imprimo la lista


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

#temperaturas = [          #matriz con temperaturas minimas y maximas por dia
#[2,14],
#[4,15],
#[1,12],
#[0,8],
#[6,15],
#[7,16],
#[9,9],
#] 

#minima= [fila[0] for fila in temperaturas]   #recorro buscando el numero mas chico
#maxima = [fila[1] for fila in temperaturas]  #recorro buscando el numero mas grande

#promedio_min=sum(minima)/len(minima)   #suma todos los numeros dividido cantidad de temperaturas
#promedio_max=sum (maxima)/len(maxima)  

#print("El promedio de la temperatura minima fue: ", promedio_min , "grados") #imprimo el promedio minimo
#print("El promedio de la temperatura maxima fue: " , promedio_max , "grados") #imprimo el promedio maximo

#amplitud = [fila[1]-fila[0] for fila in temperaturas]  #calculo la amplit o mayor diferencia de temperatura entre min y max
#dia_mayor_amplitud = amplitud.index(max(amplitud))+1    #busco el dia con mayor amplitud
#print("El dia con mayor aplitud fue el: ", dia_mayor_amplitud)   #imprimo el dia el cual fue el dia 1

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

#notas =[             #Matriz con 5 estudiantes con notas de 3 materias
#    [7, 8, 9],
#    [6, 5, 7],
#    [8, 9, 10],
#    [5, 6, 5],
#    [9, 8, 7]
#]

#print("Notas de estudiantes: ")
#for fila in notas:
#    for nota in fila:
#        print(nota, end=", ")
#    print()

#print("Promedio de cada estudiante")

#for i in range(5):
#    suma = 0
#    for j in range(3):
#        suma += notas [i][j]
#        promedio = suma / 3
#    print(f"Estudiante {i+1}:{promedio:.2f}")

#promedio por cada materia:

#for j in range (3):
#    suma = 0
#    for i in range (5):
#        suma += notas [i][j]
#    promedio = suma / 5
#    print (f"Promedio materia {j+1}:{promedio:.2f}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

#tablero = []    #lista tablero vacia

#for i in range(3):          
#    fila = []         #genero lista vacia
#    for j in range (3):
#        fila.append("-")    #cargo con - las filas
#    tablero.append(fila)

#for fila in tablero:
#    for celda in fila:
#        print(celda, end= " ")
#    print()

#Variables de control
#jugador = "X"
#jugadas = 0

#while jugadas < 9:
#    print(f"\nTurno del jugador {jugador}")
#    fila = int (input("Ingrese la fila (0-2): "))
#    columna = int (input("Ingrese la columna (0-2): "))
#    if fila<0 or fila>2 or columna<0 or columna>2:
#        print ("Posicion fuera de rango. Intente de nuevo")
#        continue #volver a pedir la jugada sin perder el turno

#    if tablero[fila][columna] == "-":
#        tablero[fila][columna] = jugador
#        jugadas +=1
#    else:
#       print("Casilla ocupada. Inente de nuevo")
#        continue  # volver a pedir la jugada sin perder el turno

#    for fila in tablero:
#        for celda in fila:
#            print(celda, end=" ")
#        print()

#    if jugador == "X":
#        jugador = "0"
#    else:
#        jugador = "X"

#TpN1/UTN-TUPaDProgramacion1/Listas/Practico 5 Sebastian Kocuta.py"
#- - - 
#- - - 
#- - -

#Turno del jugador X
#Ingrese la fila (0-2): 1
#Ingrese la columna (0-2): 1
#- - - 
#- X -
#- - -

#Turno del jugador 0
#Ingrese la fila (0-2): 1
#Ingrese la columna (0-2): 1
#Casilla ocupada. Inente de nuevo

#Turno del jugador 0
#Ingrese la fila (0-2): 0
#Ingrese la columna (0-2): 0
#0 - - 
#- X -
#- - -

#Turno del jugador X
#Ingrese la fila (0-2): 0
#Ingrese la columna (0-2): 1
#0 X - 
#- X -
#- - -

#Turno del jugador 0
#Ingrese la fila (0-2): 1
#Ingrese la columna (0-2): 0
#0 X - 
#0 X -
#- - -

#Turno del jugador X
#Ingrese la fila (0-2): 2 
#Ingrese la columna (0-2): 1
#0 X - 
#0 X -
#- X -


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

ventas = [                    #mariz de 4x7
    [5, 3, 2, 7, 6, 5, 8],    #Venta producto 1
    [4, 8, 5, 2, 9, 2, 7],    #Venta producto 2
    [8, 3, 4, 5, 6, 1, 6],    #Venta producto 3
    [1, 2, 4, 9, 8, 3, 4]     #Venta producto 4
]

#Ventas totales por producto, suma horizontal de productos
totales_productos = []

for i in range (4):
    totales_producto = 0
    for j in range (7):
        totales_producto+= ventas [i][j]
    totales_productos.append(totales_producto)
    print (f"Producto {i+1}:{totales_producto}")

#Dia con mayor ventas totales, suma verticad de productos para calcular venta de 1 dia

mayor_ventas = 0
dia_mayor = 0


#Producto mas vendido en la semana
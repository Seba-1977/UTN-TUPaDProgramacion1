#ctividades:

#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

# Crear archivo con productos
#with open("productos.txt", "w") as archivo:
#    archivo.write("Arroz,0.9,8\n")
#    archivo.write("Fideos,1.9,4\n")
#    archivo.write("Harina,1.20,10\n")

#print("Archivo 'productos.txt' creado.")
#print()

#verifico el contenido del archivo productos.txt
#print("Contendido del archivo producto.txt")

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        print(linea.strip())  


#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        
#        linea = linea.strip()
#        
#        nombre, precio, cantidad = linea.split(",")
        
#        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

#with open("productos.txt", "r") as archivo:
#    print("Lista de productos actuales:\n")
#    for linea in archivo:
#        linea = linea.strip()
#        nombre, precio, cantidad = linea.split(",")
#        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Pedir datos del nuevo producto
#print("\n Ingresar un nuevo producto")
#nombre_nuevo = input("Nombre: ")
#precio_nuevo = input("Precio: ")
#cantidad_nueva = input("Cantidad: ")

# Agregar el nuevo producto al archivo sin borrar lo anterior
#with open("productos.txt", "a") as archivo:
#    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

#print("\n Producto agregado correctamente.")

#verifico el contenido del archivo productos.txt
#print("Contendido del archivo producto.txt")

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        print(linea.strip())  

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

#productos = []  

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        linea = linea.strip()
#        nombre, precio, cantidad = linea.split(",")
#        producto = {
#            "nombre": nombre,
#            "precio": float(precio),
#            "cantidad": int(cantidad)
#        }
#        productos.append(producto)

#print("Productos cargados desde el archivo:\n")
#for p in productos:
#    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#verifico el contenido del archivo productos.txt
#print("Contendido del archivo producto.txt")

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#       print(linea.strip()) 

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

#productos = []

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        linea = linea.strip()
#        nombre, precio, cantidad = linea.split(",")
#        producto = {
#            "nombre": nombre,
#            "precio": float(precio),
#            "cantidad": int(cantidad)
#        }
#        productos.append(producto)

#nombre_buscar = input(" Ingrese el nombre del producto a buscar: ").strip()

#encontrado = False
#for p in productos:
#    if p["nombre"].lower() == nombre_buscar.lower():  
#        print(f"\n Producto encontrado:")
#        print(f"Nombre: {p['nombre']}")
#        print(f"Precio: ${p['precio']}")
#        print(f"Cantidad: {p['cantidad']}")
#        encontrado = True
#        break

#if not encontrado:
#    print(f"\n El producto '{nombre_buscar}' no existe en la lista.")

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.
#Consejo final:
#Antes de empezar, analizá cada problema y pensá cómo dividirlo en partes:
#● Leer archivo
#● Procesar datos
#● Mostrar o actualizar información
#● Guardar los cambios
#Al terminar, probá tu programa varias veces:
#● ¿Se puede agregar más de un producto?
#● ¿Se guarda todo correctamente?
#● ¿Se muestra bien el resultado?

#productos = []

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        linea = linea.strip()
#        if linea:  
#            nombre, precio, cantidad = linea.split(",")
#            producto = {
#                "nombre": nombre,
#                "precio": float(precio),
#                "cantidad": int(cantidad)
#            }
#            productos.append(producto)

#print("Productos actuales:\n")
#for p in productos:
#    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#opcion = input("\n¿Deseas agregar un nuevo producto? (s/n): ").strip().lower()
#if opcion == "s":
#    nombre = input("Nombre: ")
#    precio = float(input("Precio: "))
#    cantidad = int(input("Cantidad: "))
#    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
#    print("Producto agregado correctamente.")

#with open("productos.txt", "w") as archivo:
#    for p in productos:
#        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

#print("\n Archivo 'productos.txt' actualizado correctamente.")

#verifico el contenido del archivo productos.txt
#print("Contendido del archivo producto.txt")

#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#       print(linea.strip()) 

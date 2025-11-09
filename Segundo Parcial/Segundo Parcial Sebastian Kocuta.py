import csv
import os

nombre_archivo = "biblioteca.csv"

def ingresar_titulos_multiples():                                                            #Ingresar titulos multiples
    libros = {}
    titulos_existentes = set()
                                                                   
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:                         # Leer títulos existentes en el archivo si ya existe
            reader = csv.reader(archivo)
            for fila in reader:
                if fila:                                                                     # Evitar filas vacías
                    titulos_existentes.add(fila[0].lower())


    while True:
        n_input = input("¿Cuántos libros deseas ingresar? ")
        if n_input.isdigit() and int(n_input) > 0:
            n = int(n_input)
            break
        else:
            print("Ingresa un número entero mayor que cero.")

    for i in range(1, n + 1):
        print(f"\nLibro #{i}")

        while True:
            titulo = input("Título: ").strip()
            if titulo == "":
                print("El título no puede estar vacío.")
            else:
                titulo_lower = titulo.lower()
                libros_lower = {t.lower() for t in libros}
                existentes_lower = {t.lower() for t in titulos_existentes}

                if titulo_lower in libros_lower or titulo_lower in existentes_lower:
                    print("Este título ya fue ingresado, intente con otro.")
                else:
                    break

        while True:
            cantidad_input = input("Cantidad de ejemplares: ").strip()
            if cantidad_input.isdigit() and int(cantidad_input) >= 0:
                cantidad = int(cantidad_input)
                break
            else:
                print("Ingresa un número entero mayor o igual a 0.")            

        libros[titulo] = cantidad

    escribir_encabezado = not os.path.exists(nombre_archivo) or os.stat(nombre_archivo).st_size == 0
    with open(nombre_archivo, "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        if escribir_encabezado:
            writer.writerow(["Título", "Cantidad"])
        for titulo, cantidad in libros.items():
            writer.writerow([titulo, cantidad])


    print("\n Libros ingresados:")
    for titulo, cantidad in libros.items():
        print(f"- {titulo}: {cantidad} ejemplar(es)")

    return libros



def ingresar_ejemplares():                                                               #Ingresar Ejemplares
    if not os.path.exists(nombre_archivo):
        print("No hay libros registrados aún.")
        return

    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:                          # Leer el catálogo existente
        reader = csv.reader(archivo)
        next(reader, None)                                                                # Saltar encabezado si existe
        libros = [fila for fila in reader if fila]

    if not libros:
        print("El catálogo está vacío.")
        return

    
    catalogo = {titulo.lower(): [titulo, int(cantidad)] for titulo, cantidad in libros}    # Convertir a diccionario (clave = título en minúsculas)

    titulo = input("Ingrese el título al que desea agregar ejemplares: ").strip()
    titulo_lower = titulo.lower()

    if titulo_lower not in catalogo:
        print(f"El libro '{titulo}' no existe en el catálogo. Usa la opción 1 o 6 para registrarlo primero.")
        return

    
    while True:
        cantidad_input = input("¿Cuántos ejemplares desea agregar? ").strip()              # Pedir cantidad a agregar, asegurando que sea un número válido
        if cantidad_input.isdigit() and int(cantidad_input) > 0:
            cantidad_agregar = int(cantidad_input)
            break
        else:
            print("Ingresa un número entero mayor que 0.")

    
    catalogo[titulo_lower][1] += cantidad_agregar                                          # Sumar ejemplares

    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:              # Reescribir todo el archivo (manteniendo encabezado y datos actualizados)
        writer = csv.writer(archivo)
        writer.writerow(["Título", "Cantidad"])                                           # encabezado
        for _, (titulo_orig, cantidad) in catalogo.items():
            writer.writerow([titulo_orig, cantidad])

    print(f"Se agregaron {cantidad_agregar} ejemplar(es) a '{titulo}'. Total actual: {catalogo[titulo_lower][1]}.")




def mostrar_catalogo():                                                                   #Mostrar Calalogo
    if not os.path.exists(nombre_archivo):
        print("No hay libros registrados aún.")
        return

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader, None)
        libros = [fila for fila in reader if fila]

        if not libros:
            print("El catálogo está vacío.")
            return

        print("\n-- Catálogo completo de libros --")
        for fila in libros:
            if fila:                                                                    # Evita filas vacías
                titulo, cantidad = fila
                print(f"- {titulo}: {cantidad} ejemplar(es)")

def consultar_disponibilidad():                                                         #Consultar disponibilidad
    if not os.path.exists(nombre_archivo):
        print("No hay libros registrados aún.")
        return

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader, None)                                                             # Saltar encabezado si existe
        libros = {fila[0].lower(): int(fila[1]) for fila in reader if fila}

    if not libros:
        print("El catálogo está vacío.")
        return

    titulo = input("Ingrese el título del libro a consultar: ").strip().lower()

    if titulo in libros:
        cantidad = libros[titulo]
        if cantidad > 0:
            print(f"'{titulo.title()}' está disponible con {cantidad} ejemplar(es).")
        else:
            print(f"'{titulo.title()}' está registrado pero está agotado.")
    else:
        print(f"El libro '{titulo.title()}' no se encuentra en el catálogo.")


def listar_agotados():                                                                #Lista Agotados
    if not os.path.exists(nombre_archivo):
        print("No hay libros registrados aún.")
        return

    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:                      # Leer catálogo desde el CSV
        reader = csv.reader(archivo)
        next(reader, None)                                                            # Saltar encabezado si existe
        libros = [fila for fila in reader if fila]

    if not libros:
        print("El catálogo está vacío.")
        return

    agotados = []
    for titulo, cantidad in libros:
        
        if cantidad.isdigit() and int(cantidad) == 0:                                # Validar que cantidad sea número (por si el CSV fue modificado manualmente)
            agotados.append(titulo)

    if len(agotados) == 0:
        print("No hay libros agotados actualmente.")
    else:
        print("\n-- Libros agotados --")
        for titulo in agotados:
            print(f"- {titulo}")

def agregar_titulo():                                                                #Agregar titulos
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:     # Crear el archivo con encabezado si no existe
            writer = csv.writer(archivo)
            writer.writerow(["Título", "Cantidad"])

    
    titulos_existentes = set()                                                       # Leer títulos existentes para evitar duplicados
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader, None)
        for fila in reader:
            if fila:
                titulos_existentes.add(fila[0].lower())

    print("\n--- Alta de un nuevo libro ---")

    
    while True:
        titulo = input("Título del libro: ").strip()                                 # Validar título
        if titulo == "":
            print("El título no puede estar vacío.")
        elif titulo.lower() in titulos_existentes:
            print("Este título ya existe en el catálogo.")
        else:
            break

    
    while True:
        cantidad_input = input("Cantidad inicial de ejemplares: ").strip()          # Validar cantidad inicial
        if cantidad_input.isdigit() and int(cantidad_input) >= 0:
            cantidad = int(cantidad_input)
            break
        else:
            print("Ingresa un número entero mayor o igual a 0.")

    
    with open(nombre_archivo, "a", newline="", encoding="utf-8") as archivo:    # Agregar registro al archivo
        writer = csv.writer(archivo)
        writer.writerow([titulo, cantidad])

    print(f"Libro '{titulo}' agregado con {cantidad} ejemplar(es).")


def actualizar_ejemplares():                                                     #Actualizar ejemplares
    if not os.path.exists(nombre_archivo):
        print("No hay libros registrados aún.")
        return

    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:                    # Cargar catálogo
        reader = csv.reader(archivo)
        next(reader, None)
        catalogo = {fila[0].lower(): [fila[0], int(fila[1])] for fila in reader if fila}

    if not catalogo:
        print("El catálogo está vacío.")
        return

    titulo = input("Ingrese el título del libro: ").strip()
    titulo_lower = titulo.lower()

    if titulo_lower not in catalogo:
        print(f"El libro '{titulo}' no existe en el catálogo.")
        return

    accion = input("¿Registrar préstamo (P) o devolución (D)? ").strip().upper()
    if accion not in ("P", "D"):
        print("Opción inválida. Ingresa 'P' para préstamo o 'D' para devolución.")
        return

    if accion == "P":
        if catalogo[titulo_lower][1] > 0:
            catalogo[titulo_lower][1] -= 1
            print(f"Préstamo registrado. Queda {catalogo[titulo_lower][1]} ejemplar(es) de '{catalogo[titulo_lower][0]}'.")
        else:
            print(f"No hay ejemplares disponibles para '{catalogo[titulo_lower][0]}'.")
    else:  
        catalogo[titulo_lower][1] += 1                                            # Devolución
        print(f"Devolución registrada. Total actual: {catalogo[titulo_lower][1]} ejemplar(es) de '{catalogo[titulo_lower][0]}'.")

    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:    # Guardar cambios
        writer = csv.writer(archivo)
        writer.writerow(["Título", "Cantidad"])
        for _, (titulo_orig, cantidad) in catalogo.items():
            writer.writerow([titulo_orig, cantidad])



def mostrar_menu():                                                           #Menu de opciones numeradas
    while True:
        print("*"*40)
        print("- Biblioteca Escolar - Menu de Opciones -")
        print("*"*40)
        print("1. Ingresar títulos(multiples)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título")
        print("7. Actualizar ejemplares(préstamos/devolución):")
        print("8. Salir")
        print("*"*40)
        opcion = input ("Ingrese opcion: ").strip()

        match opcion:
            case "1":
                libros = ingresar_titulos_multiples()
            case "2":
                ingresar_ejemplares()
            case "3":
                mostrar_catalogo()
            case "4":
                consultar_disponibilidad()
            case "5":
                listar_agotados()
            case "6":
                agregar_titulo()
            case "7":
                actualizar_ejemplares()
            case "8":
                print("Gracias por haber utilizado este programa")
                break
            case _:
                print ("La opcion ingresada no en valida, por favor verifique y vuelva a intentarlo")

mostrar_menu()



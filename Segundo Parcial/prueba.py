# Programa para ingresar múltiples títulos de libros sin usar except

def ingresar_libros():
    libros = {}  # Usamos un diccionario {titulo: cantidad}

    # Pedimos la cantidad de libros que se desean ingresar
    while True:
        n_input = input("¿Cuántos libros deseas ingresar? ")
        if n_input.isdigit() and int(n_input) > 0:
            n = int(n_input)
            break
        else:
            print("❌ Ingresa un número entero mayor que cero.")

    # Ingreso de los libros
    for i in range(1, n + 1):
        print(f"\nLibro #{i}")

        # Validar título
        while True:
            titulo = input("Título: ").strip()
            if titulo == "":
                print("❌ El título no puede estar vacío.")
            elif titulo in libros:
                print("❌ Este título ya fue ingresado, intenta con otro.")
            else:
                break

        # Validar cantidad
        while True:
            cantidad_input = input("Cantidad de ejemplares: ").strip()
            if cantidad_input.isdigit():
                cantidad = int(cantidad_input)
                break
            else:
                print("❌ Ingresa un número entero mayor o igual a 0.")

        # Guardar en el diccionario
        libros[titulo] = cantidad

    # Mostrar resumen
    print("\n📚 Libros ingresados:")
    for titulo, cantidad in libros.items():
        print(f"- {titulo}: {cantidad} ejemplar(es)")

    return libros

# Ejecución del programa
if __name__ == "__main__":
    ingresar_libros()

class Libro:
    def __init__(self, libro, fecharetiro, fechadevolucion, aquien, estado):
        self.libro = libro
        self.fecharetiros = fecharetiro
        self.fechadevolucion = fechadevolucion
        self.aquien = aquien
        self.estado = estado

libros = []

def crear_libro():
    libro = input("Ingrese el título del libro: ")
    fecharetiro = input("Ingrese la fecha de retiro (YYYY-MM-DD): ")
    fechadevolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
    aquien = input("Ingrese a quién se le prestó el libro: ")
    estado = input("Ingrese el estado del libro: ")
    libro = Libro(libro, fecharetiro, fechadevolucion, aquien, estado)
    libros.append(libro)
    print("¡Libro agregado!")

def leer_libros():
    if not libros:
        print("No hay libros disponibles.")
    for libro in libros:
        print(f"Libro: {libro.libro}, Fecha Retiro: {libro.fecharetiro}, Fecha Devolución: {libro.fechadevolucion}, A quién: {libro.aquien}, Estado: {libro.estado}")

def actualizar_libro():
    libro_a_actualizar = input("Ingrese el título del libro a actualizar: ")
    for libro in libros:
        if libro.libros == libro_a_actualizar:
            libro.fecharetiro = input("Ingrese la nueva fecha de retiro (YYYY-MM-DD): ")
            libro.fechadevolucion = input("Ingrese la nueva fecha de devolución (YYYY-MM-DD): ")
            libro.aquien = input("Ingrese a quién se le prestó el libro: ")
            libro.estado = input("Ingrese el nuevo estado del libro: ")
            print("¡Libro actualizado!")
            return
    print("Libro no encontrado.")

def borrar_libro():
    libro_a_borrar = input("Ingrese el título del libro a borrar: ")
    global libros
    libros = [libro for libro in libros if libro.libro != libro_a_borrar]
    print("¡Libro borrado!")

def menu():
    while True:
        print("\nMenú de Libros")
        print("1. Crear libro")
        print("2. Leer libros")
        print("3. Actualizar libro")
        print("4. Borrar libro")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            leer_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            borrar_libro()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()

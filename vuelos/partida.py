class Partida:
    def __init__(self, id_partida, descripcion, debe, haber):
        self.id_partida = id_partida
        self.descripcion = descripcion
        self.debe = debe
        self.haber = haber

    def saldo(self):
        return self.haber - self.debe

partidas = []

def crear_partida():
    id_partida = input("Ingrese el ID de la partida: ")
    descripcion = input("Ingrese la descripción: ")
    debe = float(input("Ingrese el monto del debe: "))
    haber = float(input("Ingrese el monto del haber: "))
    partida = Partida(id_partida, descripcion, debe, haber)
    partidas.append(partida)
    print("¡Partida agregada!")

def leer_partidas():
    if not partidas:
        print("No hay partidas disponibles.")
    for partida in partidas:
        print(f"ID: {partida.id_partida}, Descripción: {partida.descripcion}, Debe: {partida.debe}, Haber: {partida.haber}, Saldo: {partida.saldo()}")

def actualizar_partida():
    id_partida = input("Ingrese el ID de la partida a actualizar: ")
    for partida in partidas:
        if partida.id_partida == id_partida:
            partida.descripcion = input("Ingrese la nueva descripción: ")
            partida.debe = float(input("Ingrese el nuevo monto del debe: "))
            partida.haber = float(input("Ingrese el nuevo monto del haber: "))
            print("¡Partida actualizada!")
            return
    print("Partida no encontrada.")

def borrar_partida():
    id_partida = input("Ingrese el ID de la partida a borrar: ")
    global partidas
    partidas = [partida for partida in partidas if partida.id_partida != id_partida]
    print("¡Partida borrada!")

def saldo_total():
    total = sum(partida.saldo() for partida in partidas)
    print(f"Saldo total de todas las partidas: {total}")

def menu():
    while True:
        print("\nMenú de Partidas")
        print("1. Crear partida")
        print("2. Leer partidas")
        print("3. Actualizar partida")
        print("4. Borrar partida")
        print("5. Ver saldo total")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_partida()
        elif opcion == "2":
            leer_partidas()
        elif opcion == "3":
            actualizar_partida()
        elif opcion == "4":
            borrar_partida()
        elif opcion == "5":
            saldo_total()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()

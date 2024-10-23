# DEFINO CLASE PRINCIPAL
# id 
# item 
# cantidad
# precio_unitario
# subtotal






class Item:
    def __init__(self,id, item, cantidad, precio_unitario, subtotal):
        self.id= id
        self.item = item
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

items = []

def crear_item():
    id = int(input("Ingrese el id: "))
    item= input("Ingrese el item: ")
    cantidad = float(input("Ingrese el cantidad: "))
    precio_unitario = float (input("Ingrese el precio_unitario: "))
    subtotal= float(input("Ingrese elsubtotal : "))
    item= Item(id, item, cantidad,precio_unitario,subtotal)
    items.append(item)
    print("item agregada!")

def leer_item():
    if not items:
        print("No hay items disponibles.")
    for item in items:

        print("id:",item .id, 
              "idem :",item.item,
              " cantidad:",item.cantidad, 
              "precio_unitario:",item.precio_unitario,
              "Subtotal",item.subtotal)

def actualizar_item():
    id= input("Ingrese el nombre del item a actualizar: ")
    for item in items:
        if item.id == id:
            item.id = input("Ingrese el nuevo id: ")
            item.cantidad = input("Ingrese la nueva cantidad: ")
            item.precio_unitario= input("Ingrese el nuevo precio_unitario: ")
            item.subtotal = input("Ingrese el nuevo subtotal: ")
            print("¡item actualizada!")
            return
    print("Item no encontrada.")

def borrar_item():
    item = input("Ingrese el nombre del item a borrar: ")
    global items
    items= [item for item in items if item.item != item]
    print("¡item borrada!")

def menu():
    while True:
        print("\nMenú de item")
        print("1. Crear item")
        print("2. Leer item")
        print("3. Actualizar item")
        print("4. Borrar item")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_item()
        elif opcion == "2":
            leer_item()
        elif opcion == "3":
            actualizar_item()
        elif opcion == "4":
            borrar_item()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
menu()


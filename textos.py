seguir=True
while seguir:
    
    # DIBUJE MENU
    print('-------------------------------------')
    print('1 - LEER TODO EL ARCHIVO')
    print('2 - GRABAR RENGLON EN ARCHIVO W')
    print('3 - AÑADIR RENGLON EN ARCHIVO A')
    print('0 - SALIR')
    
    opcion=int(input('OPCION SELECCIONADA -> '))
    
    # SI ME VOY DEL PROGRAMA
    if opcion==0:
        print('-------------------------------------')
        print('FIN...')
        break
    
    # SI AGREGO ELEMENTO AL ARREGLO
    elif opcion==1:
        print('-------------------------------------')
        nombredelarchivo=input('INGRESE NOMBRE DEL ARCHIVO --> ')
        f = open(nombredelarchivo, "r")
        print(f.read())
        f.close()
    elif opcion==2:
        print('-------------------------------------')
        nombredelarchivo=input('INGRESE NOMBRE DEL ARCHIVO --> ')
        textodelrenglon=input('INGRESE TEXTO RENGLON 1 --> ')
        f = open(nombredelarchivo, "w")
        print(f.write(textodelrenglon))
        f.close()
    elif opcion==3:
        print('-------------------------------------')
        nombredelarchivo=input('INGRESE NOMBRE DEL ARCHIVO --> ')
        textodelrenglon=input('INGRESE TEXTO RENGLON 1 --> ')
        f = open(nombredelarchivo, "a")
        print(f.write("\n"+textodelrenglon))
        f.close()
        
        
        
        



# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

# # llena la variable objeto f con el
# # contenido de la lectura archivo
# f = open("miarchivo.txt", "r")
# # para cada x dentro de f (para cada
# # renglon dentro de f)
# for x in f:
#   #imprima el renglon
#   print(x)

# #print(f.read())







# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# leer

  
# cerrar

# f.close()

# escribir y añadir

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

# -----

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# ------

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
  
#   ------
  
#  import os
# os.rmdir("myfolder")

 
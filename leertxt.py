siempre=True
while siempre==True:
    print('--------------------------------')
    print('0-Salir')
    print('1-Crea archivo y escribe un renglón')
    print('2-Leer todo un archivo')
    print('3-agregar renglon a un archivo')
    opcion=int(input('Selecciono opcion : '))
    if opcion==0:
        print('--------------------------------')
        print('Fin.')
        break
    elif opcion==1:
        print('--------------------------------')
        nombredearchivo=input('El archivo se llamará : ')
        f=open(nombredearchivo,'w')
        renglon=input('Ingrese un renglón : ')
        f.write(renglon)
        f.close()
    elif opcion==2:
        print('--------------------------------')
        nombredearchivo=input('El archivo se llama : ')
        f=open(nombredearchivo,'r')
        print('--------------------------------')
        print(f.read())
       
    elif opcion==3:
        print('--------------------------------')
        nombredearchivo=input('El archivo se llama : ')
        f=open(nombredearchivo,'a')
        renglon=input('Ingrese un renglón : ')
        f.write("\n"+renglon)
        f.close()




# f = open("prueba.txt","a")
# f.write("\n"+'este es el tercer renglon segun creo')
# f.close
# f = open("prueba.txt","r")
# print(f.read())


# import os
# if os.path.exists("prueba.txt"):
#   os.remove("prueba.txt")
#   print("El archivo ha sido borrado")
# else:
#   print("Ese no es el nombre del archivo")


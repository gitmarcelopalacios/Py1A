arreglo=[]
siempre=True
while siempre:
    print('MENÚ')
    print('--------------------------------')
    print('0 - SALIR DE LA APP')
    print('1 - CARGAR NUEVO')
    print('2 - MOSTRAR TODOS')
    print('3 - MODIFICAR ELEMENTO')
    print('--------------------------------')
    opcion=int(input('Ingrese opcion --> '))
    if opcion==0:
        print('--------------------------------')
        print('Fin de la app.')
        break
    elif opcion==1:
        elemento=input('Ingrese opcion -->')
        arreglo.append(elemento)
    elif opcion==2:
        print('--------------------------------')
        print('LISTADO DE TODOS LOS ELEMENTOS')
        print('--------------------------------')
        indice=0
        for elemento in arreglo:
            print(indice," - ",elemento)
            indice=indice+1
        print('--------------------------------')
    elif opcion==3:
        elemento=int(input('Ingrese indice --> '))
        dato=input('Ingrese dato --> ')
        arreglo[elemento]=dato 
    elif opcion==4:
        indice=int(input('Ingrese indice --> '))
        print("SE BORRARA EL DATO ",arreglo[indice])
        arreglo.pop(indice)
  

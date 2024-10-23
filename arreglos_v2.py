# DECLARE VARIABLES
seguir=True
arreglo = []
while seguir:
    
    # DIBUJE MENU
    print('-------------------------------------')
    print('0 - SALIR')
    print('1 - CARGAR ELEMENTO')
    print('2 - MOSTRAR ELEMENTOS E INDICES')
    print('3 - MODIFICAR CONTENIDO DEL ELEMENTO')
    print('4 - CONTAR ELEMENTOS DEL ARREGLO')
    print('5 - ELIMINAR ELEMENTO POR INDICE')
    print('6 - ELIMINAR ELEMENTO POR CONTENIDO')
    
    # PEDI LA OPCION DEL MENU
    opcion=int(input('OPCION SELECCIONADA -> '))
    
    # SI ME VOY DEL PROGRAMA
    if opcion==0:
        print('-------------------------------------')
        print('FIN...')
        break
    
    # SI AGREGO ELEMENTO AL ARREGLO
    elif opcion==1:
        print('-------------------------------------')
        contenido=input('INGRESE CONTENIDO --> ')
        arreglo.append(contenido)
    
    # SI MUESTRO EL ARREGLO CON SUS INDICES    
    elif opcion==2:
        print('-------------------------------------')
        indice=0
        for elemento in arreglo:
            print(indice," - ",elemento)
            indice=indice+1
    
    # SI MODIFICO EL CONTENIDO DEL ARREGLO    
    elif opcion==3:
        print('-------------------------------------')
        indice=int(input('INGRESE INDICE --> '))
        contenido=input('INGRESE CONTENIDO --> ')
        arreglo[indice]=contenido
    
    # SI CUENTO CUANTOS ELEMENTOS HAY EN EL ARREGLO    
    elif opcion==4:
        print('-------------------------------------')
        print("EL ARREGLO TIENE ",len(arreglo)," ELEMENTOS")
    
    # SI ELIMINO EL ELEMENTO POR INDICE        
    elif opcion==5:
        print('-------------------------------------')
        indice=int(input('INGRESE INDICE --> '))
        arreglo.pop(indice)
    
    # SI ELIMINO EL ELEMENTO POR CONTENIDO    
    elif opcion==6:
        print('-------------------------------------')
        contenido=input('INGRESE EL CONTENIDO A ELIMINAR --> ')
        arreglo.remove(contenido)
        
        
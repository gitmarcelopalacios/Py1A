total=0.0
seguir=True
while seguir:
    reglade=float(input('Seleccione la regla de que numero quiere : '))
    if reglade==0:
        print('Termino el programa')
    numero=1
    while numero<11:
        
        print(reglade," por ",numero," = ",(reglade*numero))
        numero=numero+1
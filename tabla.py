seguir=True 
while seguir==True:
    reglade=int(input('ingrese que regla:'))
    if reglade==0:
        print('Chau.')
        break 
    numero=1
    while numero<11:
        print(numero,' x ',reglade,' = ',(numero*reglade))
        numero=numero+1

        


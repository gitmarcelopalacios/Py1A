# ingreso en la variable operacion caracteres
operacion = input('Ingrese la operación (+,-,*,/): ')
# pregunto si cumple la condicion de suma
if operacion=='+':
    # realizo la suma
    print('SUMAR')
    print('-------------------------------')
    t1 = input('Ingrese el primer termino: ')
    t2 = input('Ingrese el segundo termino: ')
    resultado=float(t1)+float(t2)
    print('El resultado de la suma es ',resultado)
 
elif operacion=='-':

    # realizo la resta
    print('RESTA')
    print('-------------------------------')
    t1 = input('Ingrese el primer termino: ')
    t2 = input('Ingrese el segundo termino: ')
    resultado=float(t1)-float(t2)
    print('El resultado de la resta es ',resultado)

elif operacion=='*':
    
    # realizo la multiplicacion
    print('MULTIPLICACION')
    print('-------------------------------')
    t1 = input('Ingrese el primer termino: ')
    t2 = input('Ingrese el segundo termino: ')
    resultado=float(t1)*float(t2)
    print('El resultado de la multiplicación es ',resultado)

elif operacion=='/':

    # realizo la division
    print('DIVISION')
    print('-------------------------------')
    t1 = input('Ingrese el dividendo: ')
    t2 = input('Ingrese el divisor: ')
    resultado=float(t1)/float(t2)
    print('El resultado de la division ',resultado)

else:
    print('USUARIO: SELECCION LA OPCION CORRECTA')

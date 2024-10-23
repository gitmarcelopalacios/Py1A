f=open('resultados_de_tablas.txt','w')
multiplicando=1
while multiplicando<11:
    numero=0
    while numero<11:
        f.write('\n'+str(numero)+'*'+str(multiplicando)+'='+str((numero*multiplicando)))
        numero=numero+1
    multiplicando=multiplicando+1
    
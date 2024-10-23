# Abrir el archivo en modo escritura
with open('tablas_de_multiplicar.txt', 'w') as archivo:
    # Generar las tablas de multiplicar del 1 al 10
    for i in range(1, 11):
        archivo.write(f'Tabla del {i}\n')
        for j in range(1, 11):
            archivo.write(f'{i} x {j} = {i * j}\n')
        archivo.write('\n')  # Añadir una línea en blanco entre tablas

print("Las tablas de multiplicar se han guardado en 'tablas_de_multiplicar.txt'")

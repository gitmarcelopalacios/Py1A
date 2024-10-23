
cars = ["Ford", "Volvo", "BMW","Mazda"]

cars[0] = "Toyota"

print(cars)

x = len(cars)


print(x)



print(cars[2])

 
cars.append("Honda")
 
for x in cars:
  print(x)


cars.pop(1)

print('--------')
for x in cars:
  print(x)

cars.remove("Honda")
print('--------')
for x in cars:
  print(x)


# total=0.0
# seguir=True
# while seguir==True:
#     cantidad = float(input('Cantidad: '))
#     if cantidad==0.0:
#         print('Total: ',total)
#         print('Fin.')
#         break
#     else:
#         cantidad=2
#         precio = float(input('Precio: '))
#         total=total+(cantidad*precio)
#         print(cantidad,' x ',precio,' = ',(cantidad*precio))
        


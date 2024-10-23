lectura

f = open("demofile.txt", "r")
print(f.read())

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5)) # lee primeros 5 caracteres

f = open("demofile.txt", "r")
print(f.readline()) # lee linea

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)
  
f = open("demofile.txt", "r")
print(f.readline())
f.close()

escribir

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

crear nuevo archivo

f = open("myfile.txt", "x")

crear nuevo archivo si no existe 
f = open("myfile.txt", "w")

borrar

import os
os.remove("demofile.txt")

chequear si existe  

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
borrar carpeta

import os
os.rmdir("myfolder")


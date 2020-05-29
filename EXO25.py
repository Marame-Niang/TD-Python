print("======================================================\n")
for i in range (0, 11):
    for j in range (0, i):
        print(i, end = " ")       
    print(" ")

print("======================================================\n")
nombre = 0
while (nombre < 1): 
    nombre = int(input("Veuillez entrer un nombre entier: "))

compteur = 0 
for i in range(1, nombre) :
	if (nombre % i == 0) :
	    compteur += 1
if(compteur == 1) :
	print(nombre, " est un nombre premier")
else:
    print(nombre, " n'est pas un nombre premier")

nombre = -1
somme = 0
while(nombre < 0): 
    nombre = int(input("Veuillez entrer un nombre entier "))

for i in range (1, nombre-1):
    diviseur = int(nombre % i)
    if (diviseur == 0):
	    somme = int(somme + i)

if (somme == nombre):
	print("Le nombre ",nombre, " est parfait")

else:
	print("Le nombre ",nombre, "n\'est pas parfait")
            


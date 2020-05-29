nombre = -1
somme =  0 
moyenne = 0
while(nombre < 0):
    nombre = int(input("Entrer un nombre entier "))

for i in range(1, nombre) :
	somme = int(somme + i )

print("La somme des entiers de 1 jusqu'à " , nombre , " est égale à " , somme )

if (nombre == 0):
    moyenne ="erreur"
else:
    moyenne = float (somme / nombre)

print("La moyenne est :" , moyenne)
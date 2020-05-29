a = -1
b = -1

while (a < 0):
    a = int(input("Entrer le premier nombre entier "))

while (b < 0):
    b = int(input("Entrer le premier nombre entier "))

while (a != b):
    if (a < b):
	    b = int (b - a)
    else : a = int(a - b)

print("Le PGCD de  a  et b est : " ,b)

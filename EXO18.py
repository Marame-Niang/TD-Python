a = -1
b = -1
while (a < 0):
    a = int(input("Entrer le premier nombre entier "))

while (b < 0):
    b = int(input("Entrer le premier nombre entier "))

if (a < b) :
	c = int(a)
        r = int(b % a)
else: 
    c = int(b) 
    r = int(a % b)

while (r != 0):
    d = int(c) 
    c = int(r)
    r = int (d % c)
print("Le PGCD de " , a , " et " , b , " est : " , c , "\n") 
print("Le PPCM de " , a , " et " , b , " est :" ,  ((a*b) / c))
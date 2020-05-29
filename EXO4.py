# Version 1 :
x = float (input ("Entrer un nombre réel "))
n = int (input ("Entrer un nombre entier "))

from math import pow
puissance = float (pow (x, n) )

print ("La puissance est : ", puissance)

# Version 2 :

x = float (input ("Entrer un nombre réel "))
n = int (input ("Entrer un nombre entier "))


puissance = 1
for i in range (1, n):
	puissance = puissance * x 
    

print ("La puissance est : ", puissance)
   

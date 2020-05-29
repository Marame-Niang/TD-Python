
x1 = float ( input ("Saisir l'abscisse du point A : ") )
y1 = float ( input ("Saisir l'ordonnée du point A : ") )

x2 = float ( input ("Saisir l'abscisse du point B : ") )
y2 = float ( input ("Saisir l'ordonnée du point B : ") )

from math import pow
from math import sqrt
distance = float( sqrt (pow ((x1 - x2), 2) + pow ((y1 - y2), 2) )) 
print ("La distance entre les 2 points est : ", distance)

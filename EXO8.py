from math import sqrt
a = float (input ("Entrer la valeurs de a: ") )
b = float (input ("Entrer la valeurs de b: ") )
c = float (input ("Entrer la valeurs de c: ") )

if(a == 0 and b > 0):
    print("L’équation est du premier degré, La solution est : ",(-c/b))

if(a == 0 and b == 0 and c == 0):
	print("Tout réel est solution")
else:
	delta = float ((b*b) - (4 *a*c))
	if (delta == 0) :
		x1 = x2 = float (-b / (2*a) )
		print("On a une racine double qui est " , x1)

	elif (delta > 0) :
		x1 = (float) (( (-b) - (sqrt(delta))) / (2*a))
		x2 = (float) (( (-b) + (sqrt (delta))) / (2*a))	
		print("l'équation admet 2 racines distincts réels que sont:", x1 ," et ", x2)
			
	else :
		print("l'équation n'a pas de solution dans IR ")
N = 0
croissant = 0 
decroissant = 0
i = 0

Tab = []
while (N<=0):
    N = int(input("Entrer un nombre entier "))

while (i < N):
    val = int(input(" Saisir Tab ["+ str(i) +"] : "))
    Tab.append(val)
    i+=1

i = 0
while (i < N-1):
	if(Tab[i]<=Tab[i+1]):
	    croissant += 1 
            if(Tab[i] >= Tab[i+1]):
	            decroissant += 1
    i+= 1  

if(croissant == N):
	print("Les nombres saisis sont dans l’ordre croissant")
elif(decroissant == N):
	print("Les nombres saisis sont dans l’ordre décroissant")
else:
    print("Les nombres saisis sont quelconque")
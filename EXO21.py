score = 0
utl2 = 0
utl1 = int(input(" Veuillez entrer le nombre à deviner "))

while (utl1 != utl2):
    utl2 = int(input(" deviner l’entier saisi par le premier utilisateur  "))
    if (utl1 < utl2):
   	     	print("L’entier est plus petit que ta proposition \n")
    elif (utl1 > utl2):
   	    	print("L’entier est plus grand que ta proposition \n")
else :
   		print("Vous avez donné la bonne réponse \n")
   		score = int(score + 1) 
   		print("votre score est:" , score )
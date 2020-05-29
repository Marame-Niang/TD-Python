score = 0
utl2 = 0
utl1 = int(input(" Veuillez entrer le nombre à deviner "))

while (utl1 != utl2):
    utl2 = int(input("\n deviner l’entier saisi par le premier utilisateur  "))
    if (utl1 > utl2):
	 	    print("Trop petit") 	    
    elif (utl1 < utl2):
	 	    print("Trop grand")	 	    
else:
        print("\n Vous avez donné la bonne réponse")
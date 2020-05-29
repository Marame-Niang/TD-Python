test = bool (False)
jour = int (input("Veuillez entrer un jour "))
mois = int (input("Veuillez entrer un mois "))
an = int (input("Veuillez entrer une année "))

if (jour < 1 or mois < 1 or an < 1 or jour > 31 or mois > 12):
	print("L’année est invalide 1")
else:
        if (jour > 30 and mois == 11 or mois == 4 or  mois == 6 or  mois == 9):
            print("L\’année est invalide  2")
        elif (jour > 29 and mois == 2):
            print("L\’année est invalide 3")
        elif (jour > 28 and mois == 2 and an % 4 != 0 and an % 100 != 0 and an % 400 != 0):
            print("L\’année est invalide 4")
        else:
            if (jour <= 31 and mois <= 12 and an % 4 == 0 and an % 100 == 0 and an % 400 == 0):
                print("L\’année est bissextile")		
            elif (jour <= 31 and mois <= 12 and an % 4 != 0 and an % 100 != 0 and an % 400 != 0):
	            print("L\’année n’est pas bissextile")
        
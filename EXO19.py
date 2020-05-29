somme = 0
prix = -1

while (prix != 0):    
    prix = int (input("Entrer un prix de l’article "))
    while(prix < 0):
        prix = int (input("Entrer un prix de l’article "))
    somme = int(somme + prix)
    
print("La somme des prix de cette suite d’article est : " , somme)

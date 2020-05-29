montant_euro = int (input ("Entrer le montant en euro "))  

billet20 = int (montant_euro / 20)  
billet10 = int ( (montant_euro % 20) / 10 )
billet5 = int ( ( ( (montant_euro % 20) % 10 ) / 5) ) 
piece2 = int (  ( ( ( (montant_euro % 20) % 10 ) % 5) / 2) ) 
piece1 = int (( ( ( ( (montant_euro % 20) % 10 ) % 5) % 2) / 1) )  

print("Le montant en auro est composé de : ", billet20 , " billet de 20: ")
print(billet10 , " billet de 10: ")
print(billet5 , " billet de 5: ")
print(piece2 , " piece de 2: ")
print(piece1 , " piece de 1 ")
	
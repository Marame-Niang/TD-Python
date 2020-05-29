a = int(input("Entrer le premier nombre entier "))
operant = str(input("Entrer l\'opérant "))
b = int(input("Entrer le deuxième nombre entier "))

if(operant == "+"):
	resultat = int(a + b)
elif(operant == "-"):
    resultat = int(a - b )
elif (operant == "*"):
    resultat = int(a * b )
elif (operant == "/" and b != 0):
    resultat = float(a / b )
elif(operant == '/' and b == 0):
    print("L’opération est impossible ")
    resultat = "erreur"
print("Le résultat de l’opération ", a, " ", operant, " " , b ," = " , resultat)





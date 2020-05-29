# Version 1
R1 = float (input("Entrer la première résistance "))
R2 = float (input("Entrer la deuxième résistance "))
R3 = float (input("Entrer la troisième résistance "))

rest_serie = float(R1 + R2 +R3 )
rest_paral = float ((R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)) 

print ("La résistance en série est de :", rest_serie)
print ("La résistance en parallèle est de :", rest_paral)

# Version 2
Choix = int (input("Faites votre choix "))

if (Choix == 1):
    freq = float((R1/rest_serie) + (R2/rest_serie) + (R3/rest_serie) )


if (Choix == 2 and rest_paral != 0):
    freq = float( (R1/ rest_paral)  + (R2 / rest_paral) + (R3/ rest_paral) )

elif(Choix == 2 and rest_paral == 0):
    freq = "erreur"

elif (Choix != 1 and Choix != 2) : 
        print(" Vous ne pouvez choisir que 1 ou 2")
        Choix = int (input("Faites votre choix "))


print ("La fréquence est de : ", freq )
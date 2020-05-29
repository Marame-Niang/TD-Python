Tab = []
for i in range(0, 5):
    val = int(input(" Saisir un entier  "+ str(i) +" : "))
    Tab.append(val)

Somme = 0
for i in range(5):
    Somme = Somme + Tab[i]
    
print("\n La somme est : ", Somme)
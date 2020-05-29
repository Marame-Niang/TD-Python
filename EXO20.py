plus_grand = 0 
indice = 0
Tab = []
for i in range(0,10):
    val = float(input(" Saisir Tab ["+ str(i) +"] : "))
    Tab.append(val)
    if (Tab[i] > plus_grand):
        plus_grand = Tab[i] 
        indice = i

print("le plus grand entre ces 10 nombres est : " , plus_grand , " et son rang est " , indice )
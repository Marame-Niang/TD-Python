milliard = 1000000000
N = 12
m = 2                    
FN = m
M = 0

for i in range(1, N+1):
    if(i == 1):
        M = 2              
        FN = M
    else:
        FN = M + m              
        m = M  
        M = FN 

print("le nombre de lapins au bout de " , N , " mois est : " , FN , "\n")  

while (FN <= milliard):
    N = N + 1                 
    FN = M + m                   
    m = M         
    M = FN

print("le nombre dépasse " , milliard , " au bout de " , N ," mois")
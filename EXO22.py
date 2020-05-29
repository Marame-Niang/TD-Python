
N = 0

while (N < 10 or N > 50):
    N = int(input("Entrer un nombre entier compris entre 10 et 50 "))

Tab = []  
for i in range(0, N):
        val = 0
        while (val < 1 or val > 100):
            val = int(input(" Saisir Tab ["+ str(i) +"] : "))
        Tab.append(val)
position = 0  
long_max = 1 
long_seq = 1
i = 0
while (i < N-1):
	if(Tab[i] < Tab[i+1]):
		long_seq += 1
		if(long_max  < long_seq ) :
			long_max  = long_seq
			position = i - long_seq + 2
	else:
		long_seq = 1	
	i = i + 1

long_seq = long_max  + position

print("La plus longue séquence est :")
i = position
while(i < long_seq):
	print(Tab[i], " * ",end="")
	i += 1
print("\n Elle débute à la position " , position , " et sa longueur est: " , long_max)

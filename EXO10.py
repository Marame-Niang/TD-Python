a = int(input("Entrer la valeur de a "))
b = int(input("Entrer la valeur de b "))
c = int(input("Entrer la valeur de c "))

if (a > b and b > c):
	a = int (a + c)      
	c = int(a - c)  
	a = int(a - c)

if (b > a and a > c):
	c = c + a   
	a = c - a 
	c = c - a 
	c = c + b 
	b = c - b 
	c = c - b

if (b > c and c > a):
	b = b + c   
	c = b - c        
	b = b - c

if (a > c and c > b):
	a = a + c       
	c = a - c       
	a = a - c        
	a = a + b        
	b = a - b        
	a = a - b

print("Dans l’ordre croissant on a : " , a , " " ,  b , " " , c)
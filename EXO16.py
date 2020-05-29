b = -1
a = int(input("Entrer le premier nombre entier "))
nombre = a

while(b <= 0):
    b = int(input("Entrer le deuxieme nombre entier "))

quotient = 0

while (a >= b):
    a = a - b 
    quotient = quotient + 1 

print ("La division de " , nombre , " / " , b , " est égale à : " , quotient)

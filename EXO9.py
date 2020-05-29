hd = -1
ha = -1
ma = -1
md = -1
sa = -1
sd = -1
while(hd < 0 ):
    hd = int (input ("entrer horaire de départ en h "))

while(md < 0 or md > 60):
    md = int (input ("entrer horaire de départ en mn "))

while(sd < 0 or sd > 60):
    sd = int (input ("entrer horaire de départ en s "))


while(ha < 0 ):
    ha = int (input ("entrer horaire de d'arrivée en h "))

while(ma < 0 or ma > 60):
    ma = int (input ("entrer horaire de d'arrivée en mn "))

while(sa < 0 or sa > 60):
    sa = int (input ("entrer horaire de d'arrivée en s "))

sd = int(sd + (hd*3600) + (md*60))
sa = int(sa + (ha*3600) + (ma*60))

if(ha < hd): 
	# convertir 24h en seconde		
	Jour_en_seconde = 24 * 3600   
	sa = sa + Jour_en_seconde 

ds = int(sa - sd)
dh = int(ds / 3600)
dm = int((ds % 3600) / 60)
print("la durée de vol est :  " , dh , "h : " , dm ," mn")
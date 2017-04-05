import random


def jeu(nb):
 for i in range(0,nb)   : 
   taille=(random.randint(160,200))
   poi=(taille-100)*(random.randint(7,10))/10
   print("%dcm %10.1fkg"%(taille,poi))

	


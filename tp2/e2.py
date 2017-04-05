def python(cle):
	a=0
	for i in range(len(cle)):
		a=a+ord(cle[i])*256**(len(cle)-i-1)
	print(a)
	return a
	
python('Blop')
	

def hash(mot):
	a=python(mot)
	print(a%255)
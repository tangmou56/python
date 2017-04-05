import numpy as np
import matplotlib.pyplot as plt

X=[0.04,0.057,0.049,0.030,0.148,0.696,0.636,0.262,0.383,0.247,0.657]
Y=[3432,3273,3049,3642,3394,2628,2204,2643,2192,2687,2159]
moyx=np.mean(X)
moyy=np.mean(Y)
def b1(X,Y):
	b1a=0
	b1b=0
	for i,j in zip(X,Y):
		b1a=b1a+(i-moyx)*(j-moyy)
		b1b=b1b+(i-moyx)**2
	return b1a/b1b


def b0(X,Y):
	b=b1(X,Y)
	return moyy-b*moyx



axey=[]
def	axe(n,X,Y):
	b00=b0(X,Y)
	b11=b1(X,Y)
	for i in X:
		axey.append(b00+b11*i)
		
		
		
axe(axey,X,Y)
plt.plot(X, Y,'ro',X,axey,'-')

plt.show()

def sqrt(n):
	return n**0.5

def calculr(X,Y):
	ymoy=np.mean(Y)
	xmoy=np.mean(X)
	haut=0
	bout1=0
	bout2=0
	for i,j in zip(X,Y):
		haut=haut+(i-xmoy)*(j-ymoy)
	for i,j in zip(X,Y):
		bout1=bout1+(i-xmoy)**2
		bout2=bout2+(j-ymoy)**2	
	return haut/(sqrt(bout1)*sqrt(bout2))	
print(calculr(X,Y))


def plotreg(X,Y):
	moyx=np.mean(X)
	moyy=np.mean(Y)
	axey=[]
	axe(axey,X,Y)
	plt.plot(X, Y,'ro',X,axey,'-')
	plt.show()
	
	
import os
import numpy as np
import matplotlib.pyplot as plt
list=[]



for line in open("foo"):
    list.append(line.strip('\n'))

for i, el in enumerate(list):
   list[i]=float(list[i])

som=0
n=0
for i in list:
	som=som+i
	n=n+1
moyen=som/n

a=plt.hist(list, 30, normed=True)



np.std(list)
s = np.random.normal(moyen, np.std(list), 1000)

b=plt.hist(s, 30, normed=True)
plt.show()
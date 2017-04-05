import random
import matplotlib.pyplot as plt
tab=[]

for i in range(0,100000):
	som=(random.randint(1,6))+(random.randint(1,6))+(random.randint(1,6))
	tab.append(som)
	
plt.hist(tab, 16, normed=True)
plt.show()
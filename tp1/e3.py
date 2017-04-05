import matplotlib.pyplot as plt

import numpy as np


x=np.random.binomial(20, 0.5, 10000)

plt.hist(x,20,normed=1,facecolor='g',alpha=0.75)

plt.show()
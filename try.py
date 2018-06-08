import numpy as np
import matplotlib.pyplot as plt

str = np.load("poly2.npy")
func = np.poly1d(str)
genx = np.linspace(0, 100, 1)
geny = func(genx)
plt.plot(genx, geny)
plt.show()

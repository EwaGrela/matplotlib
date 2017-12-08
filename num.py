import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt('example.txt', delimiter=',', unpack = True)

plt.plot(x,y, label="loaded from file")
plt.xlabel("plot number")
plt.ylabel("random number")
plt.legend()
plt.title("awesome data")
plt.show()
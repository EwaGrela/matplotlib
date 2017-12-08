x = [1,2,3,4]
x2 = [3,4,5,6]
y = [1,2,3,4]
y2 = [2,4,6,8]

import matplotlib.pyplot as plt

plt.bar(x,y, label="one", color="g")
plt.bar(x2,y2, label="two", color= "m")
plt.legend()
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.title("dependencies")
plt.show()
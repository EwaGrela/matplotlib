weight = [70, 68, 67, 65, 64, 62.5]
weight2 = [87, 84, 82,81.5,79, 78]
weeks = [6,5,4,3,2,1]

import matplotlib.pyplot as plt
plt.xlabel("weight")
plt.ylabel("height")
plt.title("weight loss graph")
plt.plot(weight, weeks, label ="person1")
plt.scatter(weight2, weeks, label="person2")
plt.legend()
plt.show()
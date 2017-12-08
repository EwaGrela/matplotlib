import matplotlib.pyplot as plt

#finding correlation between scores and time spend on learning
test_scores = [34,45,46,56,67,78,89,90,89,65,76,55,65,78,89,87,64,23,32,25,76,75,73,49,54,98]
time_spent =  [11,12,34,34,54,54,55,56,45,46,57,58,11,34,45,43,35,12,32,12,45,67,56,34,42,34]
plt.xlabel("time spent")
plt.ylabel("scores obtained")
plt.title("correlation between time \n spent writing \n and a score")
plt.scatter(time_spent, test_scores)
plt.show()

x = [1,2,3,4,5]
y = [2,4,6,8,10]
y2 = [6,12,18,24,30]
plt.scatter(x, y, marker ="o", color ="c")
plt.scatter(x,y2, marker ="v", color ="m")
plt.show()
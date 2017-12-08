import matplotlib.pyplot as plt

test_scores = [34,45,46,56,67,78,89,90,89,65,76,55,65,78,89,87,64,23,32,25,76,75,73,49,54,98]
x = [x for x in range(len(test_scores))]
plt.xlabel("students")
plt.ylabel("scores")
plt.title("Test scores")
bins = [10,20,30,40,50,60,70,80,90, 100]
plt.hist(test_scores, bins, histtype="bar", rwidth=0.6)
plt.show()
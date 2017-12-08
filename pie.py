import matplotlib.pyplot as plt
labels = "taxes", "overheard", "expenses"
sizes = [25, 55, 20]
colors = ["c", "m", "y"]
#when a pie chart is made, things are plotted counterclockwise
# if you need to empasize one element of your data, explode it
plt.pie(sizes, labels = labels, colors =colors, startangle=90, explode = (0,0.1,0), autopct="%1.1f%%", shadow= True)
plt.title("Company expenses")
plt.axis("equal")
plt.show()
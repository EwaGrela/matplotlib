import matplotlib.pyplot as plt
year = [1,2,3,4,5,6,7,8,9,10];

# in thousands
 
taxes = [17, 18, 20, 21, 34, 6, 12, 32, 21, 33]

# cost of production
overhead = [20,30,9,23,43,12,23,33,15,17]
entertainment = [12,22,33,21,32,44,34,12,21,23]

# hack - dodawanie legendy w wykresie typu stack:
plt.plot([],[], color= "m", label ="taxes")
plt.plot([],[], color= "c", label ="overhead")
plt.plot([],[], color= "g", label ="entertainment")
plt.stackplot(year, taxes, overhead, entertainment, colors =["m", "c", "g"])
plt.legend()
plt.xlabel("years")
plt.ylabel("costs")
plt.title("company expenses")
plt.show()
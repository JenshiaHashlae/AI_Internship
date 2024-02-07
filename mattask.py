import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Company performance over 12 months")
plt.xlabel("Workers")
plt.ylabel("Experience")

plt.show()

#female performance
x = np.array([5,7,8,7,2,4,2,1,9,6])
y = np.array([80,90,90,63,45,66,20,6,99,100])
plt.scatter(x, y,color="black")
plt.title("Female performance")
plt.xlabel("hours of study")
plt.ylabel("scores")
plt.show()

#Male performance
x = np.array([2,8,1,5,8,12,9,7,3,11])
y = np.array([100,10,84,15,90,99,90,95,94,100])
plt.scatter(x, y,color="pink")
plt.title("Male performance")
plt.xlabel("Study hours")
plt.ylabel("Marks")


plt.show()

x = np.array(["jan","feb","march","april","may","june","july","august","sept","oct","nov","dec"])
y = np.array([10,14,26,27,30,17,16,20,22,21,18,15])
plt.title("temperature fluctuations")
plt.xlabel("months")
plt.ylabel("temperature")

plt.bar(x, y, width = 0.1)
plt.show()


x = np.random.uniform(25,50,75)
y = np.random.normal(1000,1700,2500)
plt.title("ages in a population")
plt.xlabel("stages")
plt.ylabel("population")

plt.hist(x)
plt.hist(y)
plt.show() 

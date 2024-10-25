import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.xlabel("Average pulse")
plt.ylabel("calorie burnage")
plt.title("sport wathc Data")

plt.savefig("plot.png")  # Save to a file

plt.show()
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

font1 = {
    'family': 'serif',
    'color': 'blue',
    'size': 10
}

font2 = {
    'family': 'serif',
    'color': 'darkred',
    'size': 8
}

plt.xlabel("Average pulse", fontdict=font2)
plt.ylabel("Calorie burnage", fontdict=font2)
plt.title("Sport Watch Data", fontdict=font1)

plt.plot(y1, label="Y1 values")  # Plot y1
plt.plot(y2, label="Y2 values")  # Plot y2

plt.grid()  # Show grid
plt.legend()  # Show legend for the plots

plt.show()  # Display the plot

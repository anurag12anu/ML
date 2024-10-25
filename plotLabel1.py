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
    'color': 'darkred',  # Corrected typo here
    'size': 8
}

plt.plot(y1,y2)
plt.xlabel("Average pulse", fontdict=font2)
plt.ylabel("Calorie burnage", fontdict=font2)
plt.title("Sport Watch Data", fontdict=font1)  # Corrected the typo in title

  # Save the plot to a file

plt.show()  # Display the plot

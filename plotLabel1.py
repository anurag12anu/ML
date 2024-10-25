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

# Plot y1 and y2 separately as two different lines
plt.plot(y1, label='Line 1 (y1)')  # Plot y1
plt.plot(y2, label='Line 2 (y2)')  # Plot y2

plt.xlabel("Average pulse", fontdict=font2)
plt.ylabel("Calorie burnage", fontdict=font2)
plt.title("Sport Watch Data", fontdict=font1)

plt.legend()  # Add a legend to differentiate between the two lines
plt.grid()    # Add grid for better readability

plt.show()  # Display the plot

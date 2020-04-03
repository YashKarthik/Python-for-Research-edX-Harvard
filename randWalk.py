import numpy as np
import matplotlib.pyplot as plt

# Cordinates
delta_x = np.cumsum(np.random.normal(0, 1, (2, 1000000)), axis=1)
delta_X = np.cumsum(delta_x, axis=0)

# Start location
x_0 = np.array(([0], [0]))
# Full path
x_path = np.concatenate((x_0, delta_X), axis=1)

# Plotting
plt.plot(x_path[0], x_path[1], 'ro-')
plt.show()

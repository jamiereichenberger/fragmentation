# **************************************************************************
# Jamie, Tristan, Natsuki
# March 17, 2020
# CST-305 MWF 3:20
# Project 5 - Chaos in File System
# Goal: Write a program that displays fragmentation
# *********************************************************************************************

# libraries needed for modeling
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# ODE to calculate graphing of file creation vs. file deletion
# picked rho value of 17.9
def lorenz(x, y, z, s=15, r=17.9, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot



dt = 0.01
num_steps = 5000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values for how file creation vs. deletion will operate
xs[0], ys[0], zs[0] = (0, 1, -5)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("File Creation Size (KB)")
ax.set_ylabel("File Deletion Size (KB)")
ax.set_zlabel("File System Activity")
ax.set_title("Fragmentation Model")

plt.show()


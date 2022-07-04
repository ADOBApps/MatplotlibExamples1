# _*_ coding: utf-8 _*_
"""
Created on 03/07/2022
	Functions to create basic graphic using imperative and Object oriented syntax
@author: ADOB
"""

import matplotlib.pyplot as plt
import numpy as np

# Time axis (indepent var)
t = np.arange(0, 2, 0.01)

# Sin function
y = np.sin(8*np.pi*t)
y1 = np.cos(8*np.pi*t)

# Imperative syntax
plt.figure(1)
plt.clf()

# Create the plot
# plt.plot(x, y, 'go--')
# green circles and dashed line
plt.plot(t, y, "g--")
plt.plot(t, y1, "r-")

# Add title and labels to plot.
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (v)")
plt.title("Sin Wave Imperative syntax")
plt.grid(True)

# Object oriented syntax
fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(1,1,1)

# Create the plot
# red line
# ax.plot(t, y, "r-")
ax.plot(t, y)
ax.plot(t, y1)

# Add title and labels to plot.
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (v)")
ax.set_title("Sin Wave object oriented syntax")
ax.grid(True)

# Show the plot.
plt.show()
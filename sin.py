# _*_ coding: utf-8 _*_
"""
Created on 03/07/2022
	Functions to create basic graphic using imperative and Object oriented syntax
@author: ADOB
"""

#text.latex.preamble : 
	# IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
	# AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
	# IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
	# preamble is a comma separated list of LaTeX statements
	# that are included in the LaTeX document preamble.
# An example:
	# text.latex.preamble : \usepackage{bm},\usepackage{euler}
	# The following packages are always loaded with usetex, so
	# beware of package collisions: color, geometry, graphicx,
	# type1cm, textcomp. Adobe Postscript (PSSNFS) font packages
	# may also be loaded, depending on your font settings


import matplotlib.pyplot as plt
import numpy as np

# set params characteristics at all plots and subplots for implements latext
params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)


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
plt.plot(t, y, "g--", label=r'$\alpha=sin(8*\pi*t)$')
plt.plot(t, y1, "r-", label=r'$\beta=cos(8*\pi*t)$')

# Add title and labels to plot.
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (v)")
plt.title("Sin Wave Imperative syntax")

# Set legend where will be our  latex text
plt.legend(loc=0)

# Show the major grid lines with dark grey lines
plt.grid(visible=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

#----------------------------------------------------------------------------------

## Object oriented syntax
fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(1,1,1)

# Create the plot
# red line
# ax.plot(t, y, "r-")
ax.plot(t, y, label=r'$\alpha=sin(8*\pi*t)$')
ax.plot(t, y1, label=r'$\beta=cos(8*\pi*t)$')

# Add title and labels to plot.
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (v)")
ax.set_title("Sin Wave object oriented syntax")
ax.legend(loc="upper right")
ax.grid(True)

# Save image
plt.savefig("sin_demo")

# Show the plot.
plt.show()
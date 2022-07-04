# _*_ coding: utf-8 _*_
"""
Created on 04/07/2022
	Functions to create basic graphic using imperative and Object oriented syntax
@author: ADOB
================================================================================
CREATE A 2 BY 2 GRID OF SUB-PLOTS WITHIN THE SAME FIGURE.
================================================================================
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
 
import numpy as np
import matplotlib.pyplot as plt


# Set allowed latex text
params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)

## Object oriented syntax

# Data
t = np.arange(0, 2, 0.01)

# Functions
y = np.sin(8*np.pi*t)
y1 = np.cos(8*np.pi*t)
y2 = np.tan(8*np.pi*t)
#y3 = np.log(8*np.pi*(t+1))
y3 = np.log(np.abs(y2+y1-y))

# Show the major grid lines with dark grey lines
plt.grid(visible=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# Initialise the figure and a subplot axes. Each subplot sharing (showing) the
# same range of values for the x and y axis in the plots.
fig, axes = plt.subplots(2, 2, figsize=(8, 6), sharex=True, sharey=True)

# Set the title for the figure
fig.suptitle("Some trigonometric functions", fontsize=15)

# Top Left subplot
axes[0,0].plot(t, y, label=r'$\alpha=sin(8*\pi*t)$')
axes[0,0].set_title("Sin")
# Set legend where will be our  latex text
axes[0,0].legend(loc="upper left")

# Top right subplot
axes[0,1].plot(t, y1, label=r'$\beta=cos(8*\pi*t)$')
axes[0,1].set_title("Cos")
# Set legend where will be our  latex text
axes[0,1].legend(loc="upper left")

# Bottom left subplot
axes[1,0].plot(t, y2, label=r'$\gamma=tan(8*\pi*t)$')
axes[1,0].set_title("Tan")
# Set legend where will be our  latex text
axes[1,0].legend(loc="upper left")

# Bottom right subplot
axes[1,1].plot(t, y3, label=r'$\epsilon=log_{10}(\gamma+\beta-\alpha)$')
axes[1,1].set_title(r"$log_{10}$")
# Set legend where will be our  latex text
axes[1,1].legend(loc="upper left")

# Save image
plt.savefig("trigo_demo")

# Show the plot.
plt.show()
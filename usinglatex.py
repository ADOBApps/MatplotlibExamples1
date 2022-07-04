import numpy as np
import matplotlib.pyplot as plt

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

params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)
x = range(0,10)
y = [t**2 for t in x]
z = [t**2+1 for t in x]
w = np.log(z)

plt.plot(x, y, label = r'$\beta=\alpha^2$')
plt.plot(x, z, label = r'$\beta=\alpha^2+1$')
plt.plot(x, w, "--",label = r'$\epsilon=log(\alpha^2+1)$')

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')

# Set legend where will be our  latex text
plt.legend(loc=0)
plt.title("LaTeX and graphics")

# Show the major grid lines with dark grey lines
plt.grid(visible=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# Show the plot.
plt.show()
import numpy as np
import matplotlib.pyplot as plt
A = 30
a = 3.5
x = np.linspace(0.01, 5, 10000)
y = A * x**a

ax = plt.gca()
plt.plot(x, y, linewidth=2.5, color='navy', label=r'$f(x) = 30 \cdot x^{3.5}$')
plt.legend(loc='upper left')
plt.xlabel(r'x')
plt.ylabel(r'y')
ax.grid(True)
plt.title(r'Normal plot')
plt.show()
plt.clf()

xlog = np.log(x)
ylog = np.log(y)
fig = plt.figure(1)
fig.clf()
ax1 = fig.gca()
ax1.plot(xlog, ylog, linewidth=2.5, color='navy', label=r'$f(x) = 3.5\cdot x + \ln(30)$')
ax1.legend(loc='best')
ax1.set_xlabel(r'log(x)')
ax1.set_ylabel(r'log(y)')
ax1.grid(True)
ax1.set_title(r'Log-Log plot')

# Show the plot.
plt.show()

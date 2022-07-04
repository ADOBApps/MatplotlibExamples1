# _*_ coding: utf-8 _*_
"""
Created on 04/07/2022
	Functions to solve differential eqs using sympy
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy

"""

import matplotlib.pyplot as plt
import numpy as np
import sympy
from scipy import integrate

def plot_direction_field(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
	"""
	This function plot EDO's direction field
	"""
	f_np = sympy.lambdify((x, y_x), f_xy, modules='numpy')
	x_vec = np.linspace(x_lim[0], x_lim[1], 20)
	y_vec = np.linspace(y_lim[0], y_lim[1], 20)
    
	if ax is None:
		_, ax = plt.subplots(figsize=(4, 4))
    
	dx = x_vec[1] - x_vec[0]
	dy = y_vec[1] - y_vec[0]
    
	for m, xx in enumerate(x_vec):
		for n, yy in enumerate(y_vec):
			Dy = f_np(xx, yy) * dx
			Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
			Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
			ax.plot([xx - Dx/2, xx + Dx/2],
				[yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
    
	ax.axis('tight')
	ax.set_title(r"$%s$" % (sympy.latex(sympy.Eq(y(x).diff(x), f_xy))), fontsize=18)
    
	return ax

# Def vars
x = sympy.Symbol("x")
y = sympy.Function("y")

#Def function
f = y(x)**2 + x**2 -1

# Graph direction field
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
campo_dir = plot_direction_field(x, y(x), f, ax=axes)

# Condición inicial
ics = {y(0): 0}

# Resolviendo la ecuación diferencial
edo_sol = sympy.dsolve(y(x).diff(x)-f, ics=ics)
edo_sol

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# panel izquierdo - solución aproximada por Serie de potencias
plot_direction_field(x, y(x), f, ax=axes[0])
x_vec = np.linspace(-3, 3, 100)
axes[0].plot(x_vec, sympy.lambdify(x, edo_sol.rhs.removeO())(x_vec),
	'b', lw=2)

# panel derecho - Solución por método iterativo
plot_direction_field(x, y(x), f, ax=axes[1])
x_vec = np.linspace(-1, 1, 100)
axes[1].plot(x_vec, sympy.lambdify(x, edo_sol.rhs.removeO())(x_vec),
	'b', lw=2)

# Resolviendo la EDO en forma iterativa 
edo_sol_m = edo_sol_p = edo_sol
dx = 0.125

# x positivos
for x0 in np.arange(1, 2., dx):
	x_vec = np.linspace(x0, x0 + dx, 100)
	ics = {y(x0): edo_sol_p.rhs.removeO().subs(x, x0)}
	edo_sol_p = sympy.dsolve(y(x).diff(x) - f, ics=ics, n=6)
	axes[1].plot(x_vec, sympy.lambdify(x, edo_sol_p.rhs.removeO())(x_vec),
		'r', lw=2)

# x negativos
for x0 in np.arange(1, 5, dx):
	x_vec = np.linspace(-x0-dx, -x0, 100)
	ics = {y(-x0): edo_sol_m.rhs.removeO().subs(x, -x0)}
	edo_sol_m = sympy.dsolve(y(x).diff(x) - f, ics=ics, n=6)
	axes[1].plot(x_vec, sympy.lambdify(x, edo_sol_m.rhs.removeO())(x_vec),
		'r', lw=2)
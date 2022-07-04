# _*_ coding: utf-8 _*_
"""
Created on 03/07/2022
	Functions to solve differential eqs using sympy
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy

"""

import matplotlib.pyplot as plt
import numpy as np
import sympy
from scipy import integrate

# Print with math latex notation
sympy.init_printing(use_latext="mathjax")

# Solve diffential es
# define vars
x = sympy.Symbol('x')
y = sympy.Function('y')

# def eq
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x), f)

# Solve differential eq
solv = sympy.dsolve(y(x).diff(x)-f)
print(solv)
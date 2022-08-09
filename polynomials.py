import numpy as np
import matplotlib.pyplot as plt

from mycontrollers.math.mypoly import ADOBpoly

# Original data
x = [0, 1, 2, 3, 4, 5]
y = [15, 10, 9, 6, 2, 0]

if __name__ == "__main__":
	ADOBpoly(x, y, 3, "mypoly", 10)
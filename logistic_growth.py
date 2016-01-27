"""
File:	logistic_growth.py
Author:	Roland Sanford (ras9841@rit.edu)
Description:
	Used RK4 to solve for the logistic growth of a population.
	User specifies the initial population size, growth factor,
	and the carrying capacity.
Version:	Python 3.5
"""

# Imports
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

def rk4solve(y0, deriv, h):
	"""
	Input:	y0 (double)
				The initial guess at time t.
			deriv (function)
				Derivative of y that depends on y.
			h (double)
				step-size > 0.
	Output: updated guess for y (double)
	"""
	k1 = deriv(y0)
	k2 = deriv(y0+h/2.0*k1)
	k3 = deriv(y0+h/2.0*k2)
	k4 = deriv(y0+h*k3)
	return y0 + h/6.0*(k1+2.0*k2+2.0*k3+k4) 

def main():
	# Constants
	n0 = 100
	k = 250
	r = 2
	h = .1
	time = np.linspace(0,100, num = 20/h)

	# Set initial population
	pop = np.append(np.array([]), n0)
	for i in range(1, len(time)):
		n0 = pop[i-1]
		deriv = lambda n0: r*n0*(1-n0/k)
		pop = np.append(pop, rk4solve(n0, deriv, h))

	# Plot solution
	plt.figure()
	plt.plot(time, pop)
	plt.grid()
	plt.axis([0, 20, 0, 300])
	plt.show()

main()

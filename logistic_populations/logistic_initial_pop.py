"""
File:	logistic_initial_pop.py
Author:	Roland Sanford (ras9841@rit.edu)
Description:
	Used RK4 to model the logistic growth of a population.
	User specifies the initial population size, growth factor,
	and the carrying capacity. Plots the results for serval initial
	population sizes.
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
	n0 = [100, 150, 200, 300, 350, 400] 
	key = [str(num) for num in n0]
	k = 250
	r = .5
	h = .1
	time = np.linspace(0,100, num = 20/h)

	# Set initial population
	pops = []
	for nv in range(0,len(n0)):
		init = n0[nv]
		pop = np.append(np.array([]), init)
		for i in range(1, len(time)):
			y0 = pop[i-1]
			deriv = lambda nn: r*nn*(1-nn/k)
			pop = np.append(pop, rk4solve(y0, deriv, h))
		pops.append(pop)

	# Plot solution
	plt.figure()
	plt.hold(True)
	for pop in pops:
		plt.plot(time, pop)
	plt.grid()
	plt.legend(key, loc='center left', title="n0 Values", 
			fancybox=True, shadow=True, bbox_to_anchor=(0.9,0.5))
	plt.axis([0, time[-1], n0[0], n0[-1]])
	# Labels
	plt.title("Changing Inital Population")
	plt.xlabel("Time", fontsize=14)
	plt.ylabel("Population Size", fontsize=14)

	# Increase font size
	font =  {'size' : 16}
	mpl.rc = {'font' : font}
	plt.show()
	

main()

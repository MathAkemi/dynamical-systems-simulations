import matplotlib.pyplot as plt
import numpy as np
from sympy import var, plot_implicit, lambdify


###
# The purpose of this program so far is to experiment with dyanmical systems as I learn about
# them in a class I am currently taking.
###


class System():
    
    # Requires a function f for the system. The set is only R^1 for now.
    def __init__(self, f):
        self.f = f

    # Iterates f on x n times.
    def iterate(self, x, n):
        if not isinstance(n, int):
            return "n must be an integer!"
        while n > 0:
            x = self.f(x)
            n -= 1

        return x

    # Returns 1 if x is a fixed point of the system, 0 if not.
    def isFixedPoint(self, x):
        if x == self.iterate(x, 1):
            return 1
        else:
            return 0

    # Returns 1 if f is a contraction, 0 if not.
    def isContraction(self):
        # Idea: check derivative, make sure it's less than linear to show it's a contraction.


x1 = 2
x2 = 1
f1 = lambda x : x
f2 = lambda x : x**2
system1 = System(f1)
system2 = System(f2)


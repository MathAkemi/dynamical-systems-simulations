#import matplotlib.pyplot as plt
#import numpy as np
#from sympy import var, plot_implicit, lambdify


###
# The purpose of this program so far is to experiment with dyanmical systems as I learn about
# them in a class I am currently taking.
###


class System():
    
    # Requires a set (list) X and a function f.
    def __init__(self, f):
        #if isinstance(x, float) or isinstance(x, int):
        #    self.type = 0
        #elif isinstance(x, list):
        #    self.type = 1

        #I plan to work on supporting different base sets, but for now I'll work only in R and R^n.

        #if x == "R":
        #    self.set = "R"
        #if x == "S1":
        #    self.set = "S1"
        #else:
        #    raise Exception("Currently only the unit circle and the real field are supported as base sets.")
        self.f = f

    def iterate(self, x, n):
        if not isinstance(n, int):
            return "n must be an integer!"
        while n > 0:
            x = self.f(x)
            n -= 1

        return x

    def isFixedPoint(self, x):
        if x == self.iterate(x, 1):
            return 1
        else:
            return 0


x1 = 2
x2 = 1
f1 = lambda x : x
f2 = lambda x : x**2
system1 = System(f1)
system2 = System(f2)


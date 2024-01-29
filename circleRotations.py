import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# A Rotation object stores the value of a, which is the amount by which the circle is
# to be rotated each time.
class Rotation():
    def __init__(self, a):
        self.a = a % 1      # the amount by which to rotate, a value in [0, 1)

    def rotate(self, n):
        if not isinstance(n, int):
            return("Please enter an integer number of times to rotate!")

        b = (self.a * n) % 1
        x = 0
        new_x = b

        # Plot the rotation.
        fig, ax = plt.subplots()       

        t = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(t), np.sin(t), linewidth=1)
        ax.set_title(str("Rotation: a = " + str(self.a) + " x " + str(n)))
        ax.plot([1], [0], 'b+')
        ax.plot(np.cos(b*2*np.pi), np.sin(b*2*np.pi), 'ro')
        plt.axis('equal')
        plt.show()



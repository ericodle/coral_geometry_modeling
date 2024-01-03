import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# constants
G = 1.66
rho = 1.4

# Define the range of r and e values
r = np.linspace(2, 50, 100)  # Range of semi-major axis
e_oblate = np.linspace(-0.9, 0, 100)  # Range of eccentricity for oblate
e_prolate = np.linspace(0, 0.9, 100)  # Range of eccentricity for prolate

# Define the range of h and a values
h = np.linspace(2, 50, 100)  # Range of semi-major axis
a = np.linspace(0, 10, 100)  # Range of eccentricity for oblate

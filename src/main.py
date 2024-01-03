# main.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions import *
from plotting import *

def main():
    # Set your constants (G, rho, etc.)
    G = 1.66
    rho = 1.4

    # Generate plots for hemispheroid surface area productivity
    imports.hemispheroid_SAP()

    # Generate plots for hemispheroid planar area productivity
    imports.hemispheroid_PAP()

    # Generate plots for hemispheroid surface area to volume ratio
    imports.hemispheroid_SVR()

    # Generate plots for branching coral surface area productivity
    imports.branching_SAP()

    # Generate plots for branching coral surface area to volume ratio
    imports.branching_SVR()

if __name__ == '__main__':
    main()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#HEMISPHERE

def hemisphere_surface(r, e, G, rho):
    S_2 = (((3 * G * r**2)/(rho)) + r**3)**(2/3)
    S_1 = r**2
    return (S_2/S_1) - 1

def hemisphere_planar(r, e, G, rho):
    S_2 = (((3 * G * r**2)/(rho)) + r**3)**(2/3)
    S_1 = 2 * r**2
    return (S_2/S_1) - 0.5

def hemisphere_svr(r):
    return 3/r

#PROLATE

def prolate_c(r, e):
    return r/np.sqrt(1 - e**2)

def J(e):
    return 1 + (np.arcsin(e)/(e * np.sqrt(1 - e**2)))

def prolate_surface(r, e, G, rho):
    S_2 = (r**3 + ((r**2 * 3 * G * J(e) * np.sqrt(1 - e**2))/(2 * rho)))**(2/3)
    S_1 = r**2
    return (S_2/S_1) - 1

def prolate_planar(r, e, G, rho):
    S_2 = (r**3 + ((r**2 * 3 * G * J(e) * np.sqrt(1 - e**2))/(2 * rho)))**(2/3) - r**2
    S_1 = r**2 * J(e)
    return (S_2/S_1)

def prolate_svr(r, e):
    return (3 / (2*prolate_c(r, e))) + ((3 * np.arcsin(e)) / (2*r*e))

#OBLATE

def oblate_c(r, e):
    return r*np.sqrt(1 - e**2)

def K(e):
    return ((1 - e**2) / (2 * e)) * np.log((1 + e) / (1 - e))

def oblate_surface(r, e, G, rho):
    S_2 = (r**3 + (3 * G * r**2 * (1+K(e))) / (2 * rho * np.sqrt(1 - e**2)))**(2/3)
    S_1 = r**2
    return (S_2/S_1) - 1

def oblate_planar(r, e, G, rho):
    S_2 = (r**3 + (3 * G * r**2 * (1+K(e))) / (2 * rho * np.sqrt(1 - e**2)))**(2/3) - r**2
    S_1 = r**2 * (1 + K(e))
    return (S_2/S_1)

def oblate_svr(r, e):
    return (3 / (2 * oblate_c(r, e))) + ((3 * oblate_c(r, e) * np.log((1 + e) / (1 - e)))/(2 * e * r**2))

# BRANCHING

def L(a):
    return a * np.sqrt(1 + (1 / a**2))

def branching_surface(h, a, G, rho):
    return (((3 * G * L(a)) / (h * rho)) + 1)**(2/3) - 1

def branching_svr(h, a, G, rho):
    SurfArea = 3 *  L(a)
    return SurfArea / h

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

def plot_3d(fun):
    M = np.arange(-5, 5, 0.1)
    Xp = np.zeros((len(M) * len(M)), float)
    Yp = np.zeros((len(M) * len(M)), float)
    Zp = np.zeros((len(M) * len(M)), float)
    i = 0
    for x in M:
        for y in M:
            XX = np.array([x, y])
            z = fun(XX)
            Xp[i] = x
            Yp[i] = y
            Zp[i] = z
            i = i + 1
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(Xp, Yp, Zp, linewidth=0.2, antialiased=True)
    plt.show()

def Sphere(X):
    X = np.array(X)
    z = np.sum((X**2))
    return z

#X = [2,1]
#fx = Sphere(X)
#print(fx)
#plot_3d(Sphere)
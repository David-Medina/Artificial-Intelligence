import numpy as np
import math
import matplotlib.pyplot as plt

def plot_2d(fun):
    X = np.arange(-5, 5, 0.1)
    Y = np.zeros_like(X)
    for i in range(len(X)):
        Y[i] = fun([X[i]])
    plt.figure()
    plt.plot(X,Y)
    plt.show()

def funcion(x):
    x = np.array(x)
    for k in range(100):
        Z = x**3 + 2*x + k
        return Z    



plot_2d(funcion)

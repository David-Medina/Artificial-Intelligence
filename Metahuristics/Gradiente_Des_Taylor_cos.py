import numpy as np
import matplotlib.pyplot as plt
import math
from Dif_Hessiano import hess

n = 1000
pX = np.random.uniform(-5*math.pi,5*math.pi,(n))
pY = 6*np.cos(pX)+np.sin(pX)

def graficar_solucion(X):
  a = X[0]
  b = X[1]
  c = X[2]
  Yc = a*np.cos(pX) + b*np.sin(pX) + c
  plt.figure()
  plt.plot(pX,pY,'.')
  plt.plot(pX,Yc,'.')
  plt.show()

def funcion_error(X):
    a = X[0]
    b = X[1]
    c = X[2]
    Yc = a*np.cos(pX) + b*np.sin(pX) + c
    return np.sum((pY-Yc)**2)

eps = 1e-5
def Gradiente(X):
    n = len(X)
    g = np.zeros((n),float)
    ei = np.zeros((n),float)
    for i in range(n):
        ei[i] = 1
        g[i] = (funcion_error(X+eps*ei)-funcion_error(X))/eps
        ei[i] = 0
    return g

def gradient_descent(X):
    k=0
    maxIter = 1000
    VfX = Gradiente(X)
    nVfX = np.linalg.norm(VfX)

    while k<maxIter and nVfX > 0.01:
        print('k:',k,'f(X):',round(funcion_error(X),4),'nV',round(nVfX,3))
        graficar_solucion(X)
        print('X',X)
        p = -VfX/nVfX # Direction
        hes = hess(funcion_error,X,p) 
        alpha = - np.dot(VfX,p)/np.dot(p,hes)# Step size
        X = X + alpha*p 	# Update solution
        k += 1
        VfX = Gradiente(X)
        nVfX = np.linalg.norm(VfX)

    print('k:',k,'f(X):',round(funcion_error(X),4),'nVfX',round(nVfX,3))
    print('X',X)
    return X


X = [1,1,1]
gradient_descent(X)

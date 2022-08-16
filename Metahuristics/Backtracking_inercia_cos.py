import numpy as np
import matplotlib.pyplot as plt
import math
from Dif_Hessiano import hess
#from Gradiente import Gradient

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


def Back(Vfx,x,p,a,m):
    c0 = 1e-4
    c1 = 2
    c2 = 5
    c3 = 3
    alpha = a
    while funcion_error(x + alpha*p) > funcion_error(x) + c0*np.dot(Vfx,p):
        m = 0
        alpha = alpha/c1
        if alpha < eps:
            alpha = eps
    m = m + 1
    if m > c2:
        m = 0
        a = c3*alpha
    else:
        a = alpha

    return alpha,a,m
        

def gradient_descent(X):
    k=0
    a = 1
    m = 0
    maxIter = 1000
    VfX = Gradiente(X)
    nVfX = np.linalg.norm(VfX)
    while k<maxIter and nVfX > 0.01:
        print('k:',k,'f(X):',round(funcion_error(X),4),'nV',round(nVfX,3))
        graficar_solucion(X)
        print('X',X)
        p = -VfX/nVfX # Direction
        #hes = hess(funcion_error,X,p) 
        alpha,a,m = Back(VfX,X,p,a,m)#-np.dot(VfX,p)/np.dot(p,hes)# Step size
        X = X + alpha*p 	# Update solution
        k += 1
        VfX = Gradiente(X)
        nVfX = np.linalg.norm(VfX)

    print('k:',k,'f(X):',round(funcion_error(X),4),'nVfX',round(nVfX,3))
    print('X',X)
    return X


X = [1,1,1]
gradient_descent(X)

import numpy as np
import matplotlib.pyplot as plt

n = 50
pX = np.random.uniform(0,10,(n))
pY = 5*pX + 10 + np.random.normal(0,3,(50))

def graficar_solucion(X):
  m = X[0]
  b = X[1]
  plt.figure()
  plt.plot(pX,pY,'.')
  plt.plot([0,10],[0*m+b,10*m+b])
  plt.show()

def funcion_error(X):
  m = X[0]
  b = X[1]
  Yc = m*pX+b
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
        if k%100==0:
            graficar_solucion(X)
        print('X',X)
        alpha = 0.01 		# Step size
        p = -VfX/nVfX 			# Direction
        X = X + alpha*p 	# Update solution
        k += 1
        VfX = Gradiente(X)
        nVfX = np.linalg.norm(VfX)

    print('k:',k,'f(X):',round(funcion_error(X),4),'nVfX',round(nVfX,3))
    print('X',X)
    return X

X = [1,1]
gradient_descent(X)



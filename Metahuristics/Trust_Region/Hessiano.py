import numpy as np 


eps = 1e-5
def vf(f,X):
    n = len(X)
    g = np.zeros((n),float)
    ei = np.zeros((n),float)
    for i in range(n):
        ei[i] = 1 
        g[i] = (f(X+eps*ei)-f(X))/eps
        ei[i] = 0
    return g

def hess(f,X):
    n = len(X)
    h = np.zeros((n,n),float)
    ei = np.zeros((n),float)
    for i in range(n):
        ei[i] = 1 
        h[i,:] = (vf(f,X+eps*ei)-vf(f,X))/eps
        ei[i] = 0
    return h


def f1(X):
    x = X[0]
    y = X[1]
    return x**3 + 2*y**2

#vf1 = vf(f1,[2,2])
#print(vf1)
#v2f1 = hess(f1,[2.,2.])
#print(v2f1)

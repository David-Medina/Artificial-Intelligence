import numpy as np 


eps = 1e-5
def Gradient(f,X):
    n = len(X)
    g = np.zeros((n),float)
    ei = np.zeros((n),float)
    for i in range(n):
        ei[i] = 1 
        g[i] = (f(X+eps*ei)-f(X))/eps
        ei[i] = 0
    return g

def f1(X):
    x = X[0]
    y = X[1]
    return x**3 + 2*y**2

#vf1 = vf(f1,[2,2])
#print(vf1)
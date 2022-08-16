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


def hess(f,X,D):
    x = np.array(X)
    d = np.array(D)
    return (vf(f,x+eps*d)-vf(f,x))/eps


def f1(X):
    x = X[0]
    y = X[1]
    return (x**3)*y

#v2f1 = hess(f1,[2,1],[4,3])
#print(v2f1)

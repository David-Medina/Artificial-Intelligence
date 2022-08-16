import numpy as np 

eps = 1e-5
def Gradient(f,X,D):
    x = np.array(X)
    d = np.array(D)
    return (f(x+eps*d)-f(x))/eps

def f1(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return (x**2)*y + z**3

#vf1 = vf(f1,[2,1,-1],[4,5,6])
#print(vf1) 
import numpy as np
from Gradiente import Gradient
from Hessiano import hess

eps = 1e-5
def McCormick(X):
    x = X[0]
    y = X[1]
    return np.sum(np.sin(x+y)+(x-y)**2 - 1.5*x + 2.5*y + 1)

def M(x,vf,p,vf2):
    vp = np.matmul(vf2,p)
    m = McCormick(x) + np.dot(vf,p) + 0.5*np.dot(p,vp)
    return m

def trust_reg(X,f):
    print("trust region")
    I = np.identity(len(X))
    MaxIter = 100
    delta = 0.1
    deltaM = 0.1
    eta = 0.25
    Vfx = Gradient(f,X)
    V2fx = hess(f,X)
    nVfx = np.linalg.norm(Vfx)
    k = 0
    while k < MaxIter and nVfx > eps:
        print(k,"f(X)",f(X))
        Bk = V2fx + 0.01*I
        Pb = -np.matmul(np.linalg.inv(Bk),Vfx)
        Pu = -Vfx/nVfx
        if np.linalg.norm(Pb) <= delta:
            Pk = Pb
            pgrad = False
        else:
            Pk = delta*Pu
            pgrad = True

        Mk = M(X,Vfx,Pk,V2fx)
        Mc = f(X)
        
        Rk = (f(X) - f(X + Pk))/(Mc - Mk)
        #print('Rk',Rk)
        if Rk < 0.25:#(1/4):
            delta = eta*delta
        elif Rk > 0.75 and pgrad:#(3/4) and pgrad:
            delta = min(2*delta,deltaM)
          
        if Rk > 0.25:#(1/4):
            X = X + Pk
            Vfx = Gradient(f,X)
            V2fx = hess(f,X)
            nVfx = np.linalg.norm(Vfx)
        k+=1

    return X



Xs = [4,4]
Xs = trust_reg(Xs,McCormick)

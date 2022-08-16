import pandas
import matplotlib.pyplot as plt
import numpy as np
from Gradiente import Gradient
from Hessiano import hess

df = pandas.read_csv('/Users/david/OneDrive/Documentos/Inteligencia artificial/5 Semestre/Optimizacion y Metaheuristicas 1/Gradiente y hessiano/Trust_Region/datos4.csv') 
#print(df)
Xp = df.values[:,0]
Yp = df.values[:,1]


eps = 1e-5
def funcion(X):
    n = int(len(X)/3)
    A = np.array(X[:n])
    C = np.array(X[n:2*n])
    D = np.array(X[2*n:])
    Yc = np.zeros_like(Yp)
    for i in range(n):
        Yc += A[i]*np.exp( -(Xp - C[i])**2 /(2*D[i]**2))
    return Yc

def graficar_solucion(X):
    Yc = funcion(X)
    plt.plot(Xp,Yc)
    plt.plot(Xp,Yp,'.')
    plt.show()

def error(X):
    Yc = funcion(X)
    return np.sum(((Yc - Yp)**2)/len(Yp))

def M(x,vf,p,vf2):
    vp = np.matmul(vf2,p)
    m = error(x) + np.dot(vf,p) + 0.5*np.dot(p,vp)
    return m

def trust_reg(X,f):
    print("trust region")
    I = np.identity(len(X))
    MaxIter = 1000
    delta = 1
    deltaM = 1
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
        if Rk < (1/4):
            delta = eta*delta
        elif Rk > (3/4) and pgrad:
            delta = min(2*delta,deltaM)
          
        if Rk > (1/4):
            X = X + Pk
            Vfx = Gradient(f,X)
            V2fx = hess(f,X)
            nVfx = np.linalg.norm(Vfx)
        k+=1
        if k%80==0:
            graficar_solucion(X)

    return X



d = 100
X = [40,25,-10,10,35,150,400,600,800,1000,d,d,d,d,d]
X = trust_reg(X,error)

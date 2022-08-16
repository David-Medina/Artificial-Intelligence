import math
from prettytable import PrettyTable
import sympy as sy
import numpy as np 


tabla = PrettyTable()
def Imprimir(n,p):
    tabla.field_names = ["N","P"]
    tabla.add_row([n,p])  

eps = 1e-2
def evaluar(fx,p):
    fx_ = sy.sympify(fx)
    y = sy.Symbol('x')
    fpx = sy.diff(fx)
    res = p - (fx_.evalf(subs={y:p})/fpx.evalf(subs={y:p}))
    return res
    
   
res = []
def Horner(P,fx,n):
    raiz = Newton(fx,P)
    print(raiz)
    x0 = raiz
    fxpol = sy.Poly(fx)
    a = fxpol.all_coeffs()
    a.reverse()
    b = np.zeros((len(a)),float)
    b[len(a)-1] = a[n]
    ite = n-1
    while ite > 0:
        b[ite] = a[ite] + b[ite+1]*x0
        ite -=1

    res.append(raiz)
    b = b[::-1]
    b = np.delete(b,len(b)-1)
    #print(b)
    x_ = sy.symbols("x")
    pol = sy.Poly(b,x_)
    #print(pol)
    if n>0:
        Horner(P,pol,n-1)
    else:
        return res
    
def Newton(fx,P0):
    cont = 0
    n = 100
    Tol = 1e-3
    i = 1 
    while i <= n:
        cont +=1
        p = evaluar(fx,P0)
        Imprimir(cont,p)
        if abs(p-P0) <= Tol:
            print(tabla)
            return p 
        else:
            i = i + 1 
            P0 = p        
    return False


fx = input("fx: ")
P0 = float(input('P0: '))
N = int(input("N: "))
print(str(Horner(P0,fx,N)))
import cmath as cm
import numpy as np
import sympy as sy
from prettytable import PrettyTable

tabla = PrettyTable()
def Imprimir(n,p):
    tabla.field_names = ["N","P"]
    tabla.add_row([n,p])  

def funcion(fx,p):
    fx_ = sy.sympify(fx)
    y = sy.Symbol('x')
    res = fx_.evalf(subs={y:p})
    return res


def Muller(fx,cero,uno,dos):
    Tol = 1e-5
    error = 1
    tres = 0
    cont = 0
    while error > Tol:
        cont +=1
        b = ((cero - dos)**2 * (funcion(fx,uno)-funcion(fx,dos)) - (uno-dos)**2 * (funcion(fx,cero)-funcion(fx,dos)))/((cero-dos)*(uno-dos)*(cero-uno))
        a = ((uno-dos)*(funcion(fx,cero)-funcion(fx,dos))-(cero-dos)*(funcion(fx,uno)-funcion(fx,dos)))/((cero-dos)*(uno-dos)*(cero-uno))
        c = funcion(fx,dos)
        b = complex(b)
        #print("a: ",a)
        #print("b",b)
        #print("c",c)
        if b.real > 0:
            tres = (-2*c)/(b+(b**2-4*a*c)**0.5 ) + dos
            
        else:
            tres = (-2*c)/(b-(b**2-4*a*c)**0.5 ) + dos
            
        tres = complex(tres)
        error = abs(tres-dos)
        cero = uno
        uno = dos
        dos = tres
        #Imprimir(cont,tres) 
    #print(tabla)
    return tres

res = []
def Horner(fx,n,cero,uno,dos):
    raiz = Muller(fx,cero,uno,dos)
    print(raiz)
    mil = raiz
    fxpol = sy.Poly(fx)
    a = fxpol.all_coeffs()
    a.reverse()
    b = [0]*(n+1)
    b[len(a)-1] = a[n]
    ite = n-1
    while ite > 0:
        b[ite] = a[ite] + b[ite+1]*mil
        ite -=1

    res.append(raiz)
    b.reverse()
    b.pop()
    #print(b)
    x_ = sy.symbols("x")
    pol = sy.Poly(b,x_)
    #print(pol)
    if n>0:
        Horner(pol,n-1,cero,uno,dos)
    else:
        return res
    


fx = input("fx: ")
N  = int(input("N: "))
x0 = float(input("x0: ")) 
x1 = float(input("x1: "))
x2 = float(input("x2: "))
print(str(Horner(fx,N,x0,x1,x2)))
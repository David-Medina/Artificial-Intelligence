import math
from prettytable import PrettyTable
import sympy as sy

def funciones(fx,p):
    #fx = x**3  + 2*x**2 - 1 
    fx_ = sy.sympify(fx)
    y = sy.Symbol('x')
    fpx = sy.diff(fx)
    res = p - (fx_.evalf(subs={y:p})/fpx.evalf(subs={y:p}))
    return res

tabla = PrettyTable()
def Imprimir(n,p):
    tabla.field_names = ["N","P"]
    tabla.add_row([n,p])    

def Newton(fx,P0):
    cont = 0
    n = 100
    Tol = 10e-5
    i = 1 
    while i <= n:
        cont +=1
        p = funciones(fx,P0)
        Imprimir(cont,p)
        if abs(p-P0) <= Tol:
            print(tabla)
            return p 
        else:
            i = i + 1 
            P0 = p        
    return False

fx = input("fx: ")
P0 = float(input("Pi:"))
print("Newton: "+str(Newton(P0)))









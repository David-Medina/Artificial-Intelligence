import math
from prettytable import PrettyTable
import math
import sympy as sy


def funcion(fx,p):
    fx_ = sy.sympify(fx)
    y = sy.Symbol('x')
    res = fx_.evalf(subs={y:p})
    return res

x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p])    
    

def Secante(p0,p1,fx):
    cont = 0
    Tol = 1e-3
    N = 100
    i = 2
    q0 = funcion(fx,p0)
    q1 = funcion(fx,p1)
    while i <= N:
        cont +=1
        p = p1 - q1*(p1 - p0)/(q1-q0)
        Imprimir(cont,p)
        if abs(p-p1) <= Tol:
            print(x)
            return p
        else:
            i +=1
            p0 = p1
            q0 = q1
            p1 = p
            q1 = funcion(fx,p)
    return False

F = input("Fx: ")
P0 = float(input("P0:"))
P1 = float(input("P1:"))
print("El resultado de la funcion secante es: "+ str(Secante(P0,P1,F)))


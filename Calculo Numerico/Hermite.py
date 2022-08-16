from prettytable import PrettyTable
import sympy as sy

tabla = PrettyTable()
def imprimir(n,p):
    tabla.field_names  = ['N','P']
    tabla.add_row([n,p])

def funcion(fx,p):
    fx_ = sy.sympify(fx)
    y = sy.Symbol('x')
    res = fx_.evalf(subs={y:p})
    return res

def Hermite(x,fx,fpx):
    pass



X = []
F = []
Fp = []
N = int(input("Tamaño: "))
for i in range(N):
    print("X"+str(i+1)+": ")
    X.append(float(input()))
for j in range(N):
    print("f(x)"+str(j+1)+": ")
    F.append(float(input()))
for y in range(N):
    print("f'(x)"+str(y+1)+": ")
    Fp.append(float(input()))






import math
from prettytable import PrettyTable
import math

def funcion(x):
    #fx = (1+x/2)*(x/1-x+x**2)**21
    #fx = 2*x * math.cos(2*x) - (x-2)**2
    fx = (1/16**2 * x**8 )- (293/32*x**6) + (119425/16*x**4) - (2451250*x**2)+ 276234375
    return fx

x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p])    
    

def Secante(p0,p1):
    cont = 0
    Tol = 1e-5
    N = 100
    i = 2
    q0 = funcion(p0)
    q1 = funcion(p1)
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
            q1 = funcion(p)
    return False

P0 = float(input("P0:"))
P1 = float(input("P1:"))
print("El resultado de la funcion secante es: "+ str(Secante(P0,P1)))


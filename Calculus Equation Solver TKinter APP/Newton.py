import math
from prettytable import PrettyTable

def funciones(x):
    #fx = x**3  + 2*x**2 - 1 
    #fpx = 3*x**2 + 4*x
    #Ejercicio 5 inciso c
    #fx = x - math.cos(x)
    #fpx = math.sin(x) + 1 
    #res = x - (fx/fpx)
    #Inciso d ejericio 5
    #fx = x - 0.8 - 0.2 * math.sin(x) 
    #fpx = math.cos(x)
    #res = x - (fx/fpx)
    #Ejericio 25 
    fx = 3**(3*x+1) - 7 * 5**(2*x)
    fpx = 3**(3*x+2) * math.log(3) - 14 * (25**x)*math.log(5)
    res = x - (fx/fpx)
    return res

x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p])    

def Newton(P0):
    cont = 1
    n = 100
    Tol = 10e-16
    i = 1 
    while i <= n:
        cont +=1
        p = funciones(P0)
        Imprimir(cont,p)
        if abs(p-P0) <= Tol:
            print(x)
            return p 
        else:
            i = i + 1 
            P0 = p        
    return False

P0 = float(input("Pi:"))
print("Newton: "+str(Newton(P0)))









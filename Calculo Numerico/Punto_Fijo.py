import math
from prettytable import PrettyTable

def funciones(p):
    gx = 2*math.sin(math.pi*p) + p
    return gx              
 
x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p])    
    


def Fijo(p0):
    cont = 0
    Tol = 1e-2
    i = 1
    n = 100
    while i<=n:
        cont +=1
        p = funciones(p0)
        Imprimir(cont,p)
        if abs(p-p0) < Tol:
            print(x)
            return p
        else: 
            i +=1  
            p0 = p
    return False


pi = float(input("P: "))
print("Punto Fijo: "+ str(Fijo(pi)))

import math
from prettytable import PrettyTable


def F(x):
    #Ejercicio 7
    #a 0,1
    #Fx = x - (pow(2,-x))   
    #b  0,1
    #Fx = (pow(math.e,x))-(x**2)+(3*x)-2   
    #c  -3,-2 / -1,0 
    #Fx = (2*x*math.cos(2*x))-((x+1)**2) 
    #dn 0.2,0.3/1.2,1.3
    #Fx = x*m.cos(x)-2*pow(x,2)+3*x-1
    #Ejercicio 11
    #Fx = pow(x,3) - 25 
    #Ejercicio 13 
    # 1,2
    #Fx = pow(x,3) - x - 1 
    #Ejercicio 17
    # 0,1
    #L= 10 
    #r=1
    #V=12.4
    #Fx = L*(0.5*math.pi*r**2 - r**2 * math.asin(x/r) - x*(r**2 - x**2)**0.5)
    #Fx -= V
    Fx = 2*x * math.cos(2*x) - (x-2)**2
    return Fx

x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p]) 

def Biseccion(a,b):
    cont = 0
    fa = F(a)
    fb = F(b)
    Tol =  1e-4
    if fa * fb > 0:
        return False
    else:
        while  abs(b-a) > Tol:
            cont +=1
            p = (b + a)/ 2 
            Imprimir(cont,p)
            if fa*F(p) < 0:
                b = p
            else:
                a = p
    print(x)
    return p


def Valores(val1,val2):
    a = int(val1)
    b = int(val2)
    print("Biseccion: "+ str((Biseccion(a,b))))


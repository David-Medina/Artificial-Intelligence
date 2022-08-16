import math as mt

def evaluar(fx,p):
    x = p
    res = eval(fx)
    #res = x*mt.log(x)
    return res


def Integracion_Compuesta_Trapecio(fx,a,b,n):
    fa = evaluar(fx,a)
    fb = evaluar(fx,b)
    h = (b-a)/n
    xi = 0
    for i in range(1,n):
        temp = a + (i*h)
        xi += evaluar(fx,temp)
    res = (h/2)*(fa+2*xi+fb) 
    return res
    
def Integracion_Compuesta_Simpson(fx,a,b,n):
    fa = evaluar(fx,a)
    fb = evaluar(fx,b)
    h = (b-a)/n
    #x0 = fa + fb
    x1 = 0 
    x2 = 0
    for i in range(1,n):
        x = a + (i*h)
        if i%2 is 0:
            x2 += evaluar(fx,x)
        else:
            x1 += evaluar(fx,x)

    xi = (h/3)*(fa+2*x2+4*x1+fb)
    return xi



F = input("Fx: ")
A = int(input("A: "))
B = int(input("B: "))
N = int(input("N: "))
print(Integracion_Compuesta_Trapecio(F,A,B,N))
print(Integracion_Compuesta_Simpson(F,A,B,N))
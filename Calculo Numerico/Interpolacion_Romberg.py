import math as mt

def evaluar(fx,p):
    x = p
    res = eval(fx)
    #res = x*mt.log(x)
    return res


def Trapecio(fx,a,b,n):
    fa = evaluar(fx,a)
    fb = evaluar(fx,b)
    h = (b-a)/n
    xi = 0
    for i in range(1,n):
        temp = a + (i*h)
        xi += evaluar(fx,temp)
    res = (h/2)*(fa+2*xi+fb) 
    return res

def Romberg(fx,a,b):
    eps = 1e-5
    k = 10
    R = [0]*k
    er = 0
    error = 0
    for i in range(k):
        n = 2**i
        R[i] = Trapecio(fx,a,b,n)
        print(R[i])
        for j in range(1,i):
            er +=1
            R[j] = R[j] + (R[j]- R[i])/(4**j-1 - 1)
            error = R[er] - R[j]

        
    
F = input("Fx: ")
A = int(input("A: "))
B =float(input("B: "))
print(Romberg(F,A,B))
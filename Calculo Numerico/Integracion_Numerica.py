import numpy as np
import sympy as sy
import math as mt

def evaluar(fx,p):
    x = p
    res = eval(fx)
    return res

def Integracion_Cerrada(n,a,b,fx): 
    fa = evaluar(fx,a)  #(np.sin(A))**2#evaluar(F,A)
    fb = evaluar(fx,b)  #(np.sin(B))**2#evaluar(F,B)
    h = (b-a)/n #para formulas abiertas b = (b-a)/(n + 2)
    fxi = [0]*(n+1)
    temp = 0
    res = []
    for x in range(n):
        temp = (a+(x+1*h))
        fxi[x] = evaluar(fx,temp)
    if n is 1:
        res.append((h/2)*(fa+fb))
    elif n is 2:
        res.append((h/3)*(fa+4*fxi[0]+fb))
    elif n is 3:
        res.append((3*h/8)*(fa+3*fxi[0]+3*fxi[1]+fb))
    elif n is 4:
        res.append((2*h/45)*(7*fa+32*fxi[0]+12*fxi[1]+32*fxi[2]+7*fb))
    else:
        pass
    return res

def Integracion_Abierta(fa,fb,n,a,b,fx):
    h = (b-a)/(n+2) #para formulas abiertas b = (b-a)/(n + 2)
    fxi = [0]*(n+1)
    temp = 0
    res = []
    for x in range(n):
        temp = (a+x+1*h)
        fxi[x] = evaluar(fx,temp)
    if n is 0:
        res.append(2*h*(fa))
    elif n is 1:
        res.append((3*h/2)*(fa+fxi[0]))
    elif n is 2:
        res.append((4*h/3)*(2*fa-fxi[0]+2*fxi[1]))
    elif n is 3:
        res.append((5*h/24)*(11*fxi[0]+fxi[1]+fxi[2]+11*fxi[3]))
    else:
        pass
    return res
    
        




print("Que integracion va a ser cerrada [c] o abierta [a]")
tipo = input()
if tipo is 'c':
    F = input("Fc: ")        
    N = int(input("N: "))#2
    A = float(input("A: "))#0  
    B = float(input("B: "))#mt.pi/2
    print("Resultado:",Integracion_Cerrada(N,A,B,F))
elif tipo is 'a':
    F = input("Fa: ")
    N = int(input("N:"))
    A = float(input("A:"))#1#0  
    B = float(input("B:"))#10#(np.pi/2)
    Fa = evaluar(F,A)#1/A#(np.sin(A))**2
    Fb = evaluar(F,B)#1/B#(np.sin(B))**2
    print("Resultado:",Integracion_Abierta(Fa,Fb,N,A,B,F))
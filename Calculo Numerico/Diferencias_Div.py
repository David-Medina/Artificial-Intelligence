import sympy as sy
import math as mt 
import numpy as np



def Dif_Div(x,fx):
    #Fi = np.zeros_like(fx)
    n = len(fx)
    matriz = [[0 for x in range(n+1)] for y in range(n)]
    print(matriz)
    for valor in range(len(x)): 
        matriz[valor][0] = fx[valor][0]
        matriz[valor][1] = fx[valor][1]
    print(matriz)
    k = 1
    for i in range(2,len(fx)+1):
        for j in range(len(fx)):
            if j+k < len(fx):
                matriz[j][i] = (fx[j+1][i-1] - fx[j][i-1])/(fx[j+k][0]-fx[j][0])
        k +=1
    return fx

X = [0.0,0.2,0.4,0.6,0.8]
Fx = [[0.0,1.00000],[0.2,1.22140],[0.4,1.49182],[0.6,1.82212],[0.8,2.22554]]
print(Dif_Div(X,Fx))
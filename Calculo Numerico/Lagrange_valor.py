import math
import sympy as sy


def funcion(y,p):
    #print(x)
    x = p
    res = eval(y)
    #print(res)
    return res

def lagrange(fx,x,n,p):
    L = ['']*n
    cont = 0
    pol = ['']*n
    div = ''
    res = ['']*n
    for i in range(n):
        cont = 0
        for y in range(n):
            if i != y:
                cont +=1
                L[i] +="((x-"+str(x[y])+")"
                if div != "":
                    if cont == n-1:
                        div = "/("+str(x[i])+"-"+str(x[y])+"))"
                    else:
                        div = "/("+str(x[i])+"-"+str(x[y])+"))" + "+"
                else:
                    div = "/("+str(x[i])+"-"+str(x[y])+"))" + "+"
                L[i] += div
                #print(cont,": ",str(L[i]))

        pol[i] += "("+L[i]+")*("+str(x[i])+")"
        res[i] = str(funcion(pol[i],x[i]))
        print(pol[i])
    return res






X = [8.1,8.3,8.6,8.7]
F = [16.94410,17.56492,18.50515,18.82091]
N = int(input("Tamaño: "))
P = float(input("P: "))
print(str(lagrange(F,X,N,P)))
import math as mt
def Diferencial(fx,x,n,h):
    for3 = []
    for5 = []
    k = 0
    for i in range(len(x)):
        h = h
        if n <= 4:
            if k is 0:
                for3.append((1/(2*h))*(-3*fx[i]+4*fx[i+1]-fx[i+2]))
            elif k is len(fx):
                h = -h
                for3.append((1/(2*h))*(-3*fx[i]+4*fx[i-1]-fx[i-2]))
            else:
                if k is len(fx)-1:
                    h = -h
                    for3.append((1/(2*h))*(-3*fx[i]+4*fx[i-1]-fx[i-2]))
                else:
                    for3.append((1/(2*h))*(fx[i+1]-fx[i-1]))
            k+=1
        elif n >=5:
            if k is 0:
                for5.append((1/(12*h))*((-25*fx[i])+(48*fx[i+1])-(36*fx[i+2])+(16*fx[i+3])-(3*fx[i+4])))
                for3.append((1/(2*h))*(-3*fx[i]+4*fx[i+1]-fx[i+2]))
            elif k is len(fx):
                h = -h
                for5.append((1/(12*h))*((-25*fx[i])+(48*fx[i-1])-(36*fx[i-2])+(16*fx[i-3])-(3*fx[i-4])))
                for3.append((1/(2*h))*(-3*fx[i]+4*fx[i-1]-fx[i-2]))
            else:
                if k >= len(fx)-2:
                    h = -h
                    for5.append((1/(12*h))*((-25*fx[i])+(48*fx[i-1])-(36*fx[i-2])+(16*fx[i-3])-(3*fx[i-4])))
                    for3.append((1/(2*h))*(-3*fx[i]+4*fx[i-1]-fx[i-2]))   
                else:
                    for5.append((1/(12*h))*((fx[i-2])-(8*fx[i-1])+(8*fx[i+1])-(fx[i+2])))
                    for3.append((1/(2*h))*(fx[i+1]-fx[i-1]))   
            k +=1
    return for3,for5



N = int(input("N:"))
X = []
F = []
for i in range(N):
    print("X",i+1,":")
    X.append(float(input()))
    print("Fx",i+1,":")
    F.append(float(input()))


H = X[1] - X[0]
tres,cinco = Diferencial(F,X,N,H)
if not tres:
    print("Funcion 5:",cinco)
elif not cinco:
    print("Funcion 3:",tres)
else:
    print("Funcion 5:",cinco)
    print("Funcion 3:",tres)
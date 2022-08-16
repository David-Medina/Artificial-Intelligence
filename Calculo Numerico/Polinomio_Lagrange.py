'''
Funcion que genera un polinomio de lagrange.
El polinomio se da ya simplificado

Para probar la funcion se utilizó el ejercicio 1
de la seccion 3.1 de analisis numerico de burden 
7 edición

'''

import sympy as sp
import math

x = sp.symbols('x')

#Funcion para generar un polinomio de lagrange 
def L(xk, xn):
    polynomial = sp.Poly(1,x)
    for xi in xn:
        polynomial*= (x - xi)/(xk - xi) if xk != xi else 1
    return polynomial

#Funcion que toma el conjnto de polinomios de lagrange
#lo multiplica por la funcion evaluada en el punto
#y suma el conjunto de polinomios 
def P(xi, f):
    polynomial = sp.Poly(0,x)
    for i in xi: 
        polynomial+= f(i)*L(i, xi)
        # print("L{}: {}".format(i, L(i, xi)))
    return sp.simplify(polynomial)

a1 = [0, 0.6]
a2 = [0, 0.6, 0.9]
def fun_a(xn):
    return math.cos(xn)
def fun_b(xn):
    return math.sqrt(1 + xn)
def fun_c(xn):
    return math.log(xn + 1)
def fun_d(xn):
    return math.tan(xn)

# print(fun_a(0.45))
print("a.")
print("P1(x) = {}".format(P(a1, fun_a).args[0]))
print("P1(0.45) = {}".format(P(a1, fun_a)(0.45)))
print("|f(0.45) - P1(0.45)| = {}".format(fun_a(0.45) - P(a1, fun_a)(0.45)))
print("----------------------")
print("P2(x) = {}".format(P(a2, fun_a).args[0]))
print("P2(0.45) = {}".format(P(a2, fun_a)(0.45)))
print("|f(0.45) - P2(0.45)| = {}".format(fun_a(0.45) - P(a2, fun_a)(0.45)))
print()

print("b.")
print("P1(x) = {}".format(P(a1, fun_b).args[0]))
print("P1(0.45) = {}".format(P(a1, fun_b)(0.45)))
print("|f(0.45) - P1(0.45)| = {}".format(fun_b(0.45) - P(a1, fun_b)(0.45)))
print("----------------------")
print("P2(x) = {}".format(P(a2, fun_b).args[0]))
print("P2(0.45) = {}".format(P(a2, fun_b)(0.45)))
print("|f(0.45) - P2(0.45)| = {}".format(fun_b(0.45) - P(a2, fun_b)(0.45)))
print()

print("c.")
print("P1(x) = {}".format(P(a1, fun_c).args[0]))
print("P1(0.45) = {}".format(P(a1, fun_c)(0.45)))
print("|f(0.45) - P1(0.45)| = {}".format(fun_c(0.45) - P(a1, fun_c)(0.45)))
print("----------------------")
print("P2(x) = {}".format(P(a2, fun_c).args[0]))
print("P2(0.45) = {}".format(P(a2, fun_c)(0.45)))
print("|f(0.45) - P2(0.45)| = {}".format(fun_c(0.45) - P(a2, fun_c)(0.45)))
print()

print("d.")
print("P1(x) = {}".format(P(a1, fun_d).args[0]))
print("P1(0.45) = {}".format(P(a1, fun_d)(0.45)))
print("|f(0.45) - P1(0.45)| = {}".format(fun_d(0.45) - P(a1, fun_d)(0.45)))
print("----------------------")
print("P2(x) = {}".format(P(a2, fun_d).args[0]))
print("P2(0.45) = {}".format(P(a2, fun_d)(0.45)))
print("|f(0.45) - P2(0.45)| = {}".format(fun_d(0.45) - P(a2, fun_d)(0.45)))
print()


# print(L(0.5, [0, 1 ,0.5]))

# X = [0, 1, 0.5]

# def f(a):
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 0
#     else:
#         return 0.5

# print(P(X, f))
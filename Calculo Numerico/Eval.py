import sympy

def funcion(x):
    return eval(fx)

def evaluar(fx):
    x = sy.symbols('x')
    #fxp = sy.diff(x**3 - 2*x**2 - 5)
    fxp = sy.diff(fx)
    fxpEval = fxp.evalf(subs={x:p})
    print(fxp,' derivada evaluada: ', fxpEval)


x = PrettyTable()
def Imprimir(n,p):
    x.field_names = ["N","P"]
    x.add_row([n,p])  

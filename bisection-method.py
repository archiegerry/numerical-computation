import numpy as np

def bisection(f, x0, x1, tol):
    it = 0
    x = (x0 + x1) / 2.
    xL = x0
    xR = x1

    y = f(x)
    yL = f(xL)
    yR = f(xR)
    while abs(y) > tol:
        if (it > 100000):
            print("Bisection Method failed to converge")
            return x, np.inf
        if y*yL < 0:
            xR = x
            yR = y
        elif y * yR < 0:
            xL = x
            yL = y
        x = (xL + xR) / 2
        y = f(x)
        it += 1
    
    return x, it

## Sometimes and m may be needed
##m = 1

## The function you want converging
def f(t):
    return t**4 - 3*t -10

## the left bracket
x0 = 0
## the right bracket
x1 = 3
## the tolerance for conversion
tol = 0.00001
solution, iteration = bisection(f, x0, x1, tol)

print(solution)
print(iteration)

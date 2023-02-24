## Sometimes and m may be needed
##m = 1

## The function you want converging
def f(t):
    return t*t*t*t - 3*t - 10

## The differential of this function
def df(t):
    return 4*t - 3

def newton(f, df, x0, tol, n):
    x = x0
    y = f(x)
    it = 0
    while abs(y) > tol and it < n:
        it += 1
        x -= y / df(x)
        y = f(x)
    return x, it

## the starting guess
x0 = 1.5

## the tolerance for conversion
tol = 0.0001

## the number of iterations you want
n = 10

solution, iteration = newton(f, df, x0, tol, n)

print(solution)
print(iteration)

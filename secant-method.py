def f(x):
    return x**4 - 3*x -10

X = np.linspace(-1., 4., num=100, endpoint=True)
Y = np.zeros(100)
for i in range(len(Y)):
    Y[i] = f(X[i])

import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(X, Y)
plt.grid()
plt.show()

def secant(f, x0, x1, tol):
    x = x1
    it = 0
    while abs(f(x)) > tol:
        x = x - f(x) * ((x - x0) / (f(x) - f(x0)))
        x0 = x1
        x1 = x
        it += 1
    return x, it

x, it = secant(f, 0.0, 1, 0.000001)
print(f"The secant method: {x} after {it} iterations")

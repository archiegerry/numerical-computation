import numpy as np

## This is the derivative function (bear in mind y(t) == d and t == t)


def f(t, d):
    return 1 - d*d

def d_exact(t):
    return 0

##  t0 = inital value of t (or x)
##  d0 = initial value of d (or y)
##  dt = step value in time
##  n  = total computational steps

t0 = float(0.0)
d0 = float(0.0)
dt = float(0.5)
n = int(1)

t_Euler, d_Euler = Euler_method(t0, d0, dt, n)
t_midpoint, d_midpoint = midpoint_method(t0, d0, dt, n)

print(t_midpoint)

print(d_midpoint)


de = np.zeros(n+1)
for i in range(n+1):
    de[i] = d_exact(t_Euler[i])
    

import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(t_Euler, d_Euler, "-b", label="Euler")
plt.plot(t_Euler, de, "-r", label="Exact")
plt.plot(t_midpoint, d_midpoint, "--g", label="midpoint")
plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("d")
plt.grid()
plt.show()

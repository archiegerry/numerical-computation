def Euler_method(t0, d0, dt, n):

##  t0 = inital value of t (or x)
##  d0 = initial value of d (or y)
##  dt = step value in time
##  n  = total computational steps

    d = np.zeros(n+1)
    d[0] = d0

    t = np.zeros(n+1)
    for i in range(n+1):
        t[i] = t0 + i * dt

    # Compute Euler's method
    for it in range(1, n+1):
        k = d[i - 1] + dt * f(t[it - 1], d[it - 1])
        d[it] = d[it - 1] + (dt/2) * f(t[it - 1], d[it - 1]) + f(it, k)

    return t, d

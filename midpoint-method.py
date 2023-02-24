def midpoint_method(t0, d0, dt, n):

##  t0 = inital value of t (or x)
##  d0 = initial value of d (or y)
##  dt = step value in time
##  n  = total computational steps

    d = np.zeros(n+1)
    d[0] = d0

    t = np.zeros(n+1)
    for i in range(n+1):
        t[i] = t0 + dt*i
    
    for i in range(1, n+1):
        k1 = f(t[i - 1], d[i - 1])
        k2 = f(t[i - 1] + (dt/2), d[i - 1] + (dt * k1/ 2))
        k3 = f(t[i - 1] + (dt/2), d[i - 1] + (dt * k2/ 2))
        k4 = f(t[i - 1] + dt, d[i - 1] + (dt * k3))
        d[i] = d[i-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    return t, d

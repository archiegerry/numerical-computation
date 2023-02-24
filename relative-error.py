import numpy as np

def relative_error(x_calc, x_real):
  return (np.abs(x_calc - x_real) / np.abs(x_real))

## The approximate stored value
x_calc = 1.4901161193847656e-08
## The real value 
x_real = 10**-8

x = relative_error(x_calc, x_real)
print (x)

import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def upper_triangular_solve(A, b):
    """
    Solve the system  A x = b  where A is assumed to be lower triangular,
    i.e. A(i,j) = 0 for j > i, and the diagonal is assumed to be nonzero,
    i.e. A(i,i) != 0.
    
    The code checks that A is lower triangular and converts A and b to
    double precision before computing.

    ARGUMENTS:  A   lower triangular n x n array
                b   right hand side column n-vector

    RETURNS:    x   column n-vector solution
    """

    # we should take care to ensure that arrays are stored with the correct type - float!
    A = A.astype(np.float64)
    b = b.astype(np.float64)
      
    # check sizes of A and b match appropriately
    nb=len(b)
    n, m = A.shape
    if n != m:
        raise ValueError(f'A is not a square matrix! {A.shape=}')
    if n != nb:
        raise ValueError(f'shapes of A and b do not match! {A.shape=} {b.shape=}')
    
    # check A is upper triangular
    for i in range(n):
        for j in range(0,i):
            if not np.isclose(A[i, j], 0.0):
                raise ValueError(f'A is not upper triangular! {A[i, j]=}')

    # checks whether A has zero diagonal element
    for i in range(n):
        if np.isclose(A[i, i], 0.0):
            raise ValueError(f'A[{i}, {i}] is zero')
    
    #create a new array to store the results
    x = np.empty_like(b)
    
    # perform backwards substitution
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(2,n+1):
        x[n-i] = b[n-i] / A[n-i, n-i]
        for j in range(n-i+1, n):
            x[n-i] = x[n-i] - A[n-i,j]*x[j] / A[n-i, n-i]
        
    return x

A = np.array([[2,1,4], [0, 1.5, 0], [0, 0, 2]])
b = np.array([12, 3, 4])
solution = upper_triangular_solve(A, b)
print(solution)

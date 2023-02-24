import numpy as np

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

def gaussian_elimination(A, b, verbose=False):
    # To ensure that arrays are stored in double precision.
    A = A.astype(np.float64)
    b = b.astype(np.float64)
     
    # size of solution vector / the square matrix A
    n=len(b) # or   n, n = A.shape
        
    # check sizes of A and b match appropriately
    nb=len(b)
    n, m = A.shape
    if n != m:
        raise ValueError(f'A is not a square matrix! {A.shape=}')
    if n != nb:
        raise ValueError(f'shapes of A and b do not match! {A.shape=} {b.shape=}')
    
    if verbose:
        print('starting system\n', A, b)

    # perform forward elimination
    for i in range(n):  
        # eliminate column i
        if verbose:
            print(f'eliminating column {i}')
        
        # check diagonal
        if np.isclose(A[i, i], 0.0):
            raise ValueError(f'A has zero on diagonal! A[{i}, {i}] = 0')

        # row j <- row j - (a_{ji} / a_{ii}) row i
        for j in range(i+1, n):
            if verbose:
                print(f'row {j} <- row {j} - {A[j, i] / A[i, i]} row {i}')
            factor = A[j, i] / A[i, i]
            for k in range(0, n):
                A[j, k] = A[j, k] - factor * A[i, k]
            b[j] = b[j] - factor * b[i]
        
        if verbose:
            print('new system\n', A, b)

    return upper_triangular_solve(A, b)   

A = np.array([[1.25, 1.5], [1.5, 3]])
b = np.array([[59.5], [94.0]])
solution = gaussian_elimination(A, b, False)
print(solution)

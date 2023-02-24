import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def gaussian_elimination_with_pivoting(A, b):
    # convert A and b to 64-bit floating point numbers
    A = A.astype(np.float64)
    b = b.astype(np.float64)

    n = A.shape[0]
    for i in range(n):
        # find the pivot element
        max_val = abs(A[i, i])
        pivot = i
        for j in range(i+1, n):
            if abs(A[j, i]) > max_val:
                max_val = abs(A[j, i])
                pivot = j
        
        # swap rows if necessary
        if pivot != i:
            A[[i, pivot], :] = A[[pivot, i], :]
            b[i], b[pivot] = b[pivot], b[i]

        for j in range(i+1, n):
            m = A[j, i]/A[i, i]
            A[j, i:] = A[j, i:] - m*A[i, i:]
            b[j] = b[j] - m*b[i]

    # back-substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/A[i, i]
    return x

# example usage
A = np.array([[1.25, 1.5], [1.5, 3]])
b = np.array([[59.5], [94.0]])
x = gaussian_elimination_with_pivoting(A, b)
print(x) 

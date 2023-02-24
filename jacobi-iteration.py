import numpy as np

def jacobi(A, b, x0, tol=1e-5, maxiter=100):
    """
    Solve a system of linear equations using the Jacobi iteration method.
    A: coefficient matrix
    b: right-hand side vector
    x0: starting guess for the solution
    tol: tolerance for the residual
    maxiter: maximum number of iterations
    """
    n = len(b)
    x = np.copy(x0)
    D = np.diag(np.diag(A))
    R = A - D
    for i in range(maxiter):
        x_prev = np.copy(x)
        x = np.dot(np.linalg.inv(D), b - np.dot(R, x))
        res = np.linalg.norm(b - np.dot(A, x))
        if res < tol:
            break
        print("Iteration {}: x = {}, residual = {}".format(i+1, x, res))
        print("\n")
    return x

A = np.array([[2, 1], [-1, 4]], dtype=np.float64)
b = np.array([3.5, 0.5], dtype=np.float64)
x0 = np.array([2, 1], dtype=np.float64)
x = jacobi(A, b, x0)

print("Solution: x = {}".format(x))

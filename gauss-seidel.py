import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    """Performs Gauss-Seidel iteration on a system of linear equations Ax = b.
    
    Parameters:
        A (np.ndarray): Coefficient matrix of the system of equations.
        b (np.ndarray): Right-hand side of the system of equations.
        x0 (np.ndarray): Initial guess for the solution.
        tol (float): Tolerance for the residual.
        max_iter (int): Maximum number of iterations.
    """
    n = len(A)
    x = x0.copy()
    x = x.astype(np.float64)
    res = np.linalg.norm(np.dot(A, x) - b)
    print("Initial residual: ", res)
    print("Initial solution: ", x)
    print("\n")
    for k in range(max_iter):
        for i in range(n):
            s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - s) / A[i, i]
        res = np.linalg.norm(np.dot(A, x) - b)
        x = x.astype(np.float64)
        print("Iteration: ", k+1)
        print("Residual: ", res)
        print("Solution: ", x)
        print("\n")
        if res <= tol:
            break


A = np.array([[4, 2], [1, 4]])
b = np.array([0, -1])
x_0 = np.array([0, -1])
tol = 1e-6
max_iter = 2


x = gauss_seidel(A, b, x_0, tol, max_iter)

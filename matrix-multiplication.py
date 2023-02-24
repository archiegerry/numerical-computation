import numpy as np

def matrix_mult(matrix1, matrix2):
    result = np.matmul(matrix1, matrix2)
    return result

# Example usage
matrix1 = np.array([[0, 0.5, 1], [1, 1, 1]])
matrix2 = np.array([[18], [33], [43]])
result = matrix_mult(matrix1, matrix2)
print(result)

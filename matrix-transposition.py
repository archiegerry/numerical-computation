import numpy as np

def matrix_mult_transpose(matrix):
    transpose = np.transpose(matrix)
    result = np.matmul(matrix, transpose)
    return result

# You MUST input the transposed matrix, not the original matrix
matrix = np.array([[0, 0.5, 1], [1, 1, 1]])
result = matrix_mult_transpose(matrix)
print(result)

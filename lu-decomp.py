from scipy.linalg import lu

def decompose_matrix(matrix):
    P, L, U = lu(matrix)
    return P, L, U

matrix = [[2, 1, 4], [1, 2, 2], [2, 4, 6]]
P, L, U = decompose_matrix(matrix)
print("Permutation: \n", P)
print("\n")
print("Lower: \n", L)
print("\n")
print("Upper: \n", U)

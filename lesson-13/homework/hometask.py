import numpy as np
print("1st task")
vector = np.arange(10, 50)
print(vector)
print("2nd task")
matrix_3x3 = np.arange(0, 9).reshape(3, 3)
print("\n2. 3x3 matrix with values 0 to 8:\n", matrix_3x3)
random_3x3x3 = np.random.random((3, 3, 3))
print("\n4. 3x3x3 array with random values is \n")
array_10x10 = np.random.random((10, 10))
min_value = array_10x10.min()
max_value = array_10x10.max()
random_vector = np.random.random(30)
mean_value = random_vector.mean()
matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product_5x3_3x2 = np.dot(matrix_5x3, matrix_3x2)
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product_3x3 = np.dot(matrix_A, matrix_B)
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
matrix_A_3x4 = np.random.random((3, 4))
matrix_B_4x3 = np.random.random((4, 3))
matrix_product_A_B = np.dot(matrix_A_3x4, matrix_B_4x3)
matrix_3x3_vec = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_vec, vector_3x1)
matrix_5x5_sum = np.random.random((5, 5))
row_sums = matrix_5x5_sum.sum(axis=1)
column_sums = matrix_5x5_sum.sum(axis=0)
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
x_solution = np.linalg.solve(A_system, b_system)
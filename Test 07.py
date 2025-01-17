import numpy as np

matrix_size = int(input("Enter the size of the matrix: "))

matrix = np.zeros((matrix_size, matrix_size))
for j in range(matrix_size):
    for i in range(matrix_size):
        matrix[i, j] = int(input(f"Enter the element at position {i+1},{j+1}: "))

# Calculate the determinant
determinant = np.linalg.det(matrix)

print(f"The determinant of the matrix is: {determinant}")
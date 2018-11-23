import random

matrix1 = [[random.randrange(100) for i in range(128)] for j in range(128)]
matrix2 = [[random.randrange(100) for i in range(128)] for j in range(128)]

result = [[0 for i in range(128)] for j in range(128)]


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")


print_matrix(matrix1)
print_matrix(matrix2)

for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print_matrix(result)

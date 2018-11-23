import random

size = 8

matrix1 = [[random.randrange(100) for i in range(size)] for j in range(size)]
matrix2 = [[random.randrange(100) for i in range(size)] for j in range(size)]
result = [[0 for i in range(size)] for j in range(size)]


for i in range(size):
    for j in range(size):
        for k in range(size):
            result[i][j] += matrix1[i][k]*matrix2[k][j]

for i in range(len(result)):
    print(result[i])

import math
import random
import copy


def generate_matrix(size):
    res = [[random.randrange(5) for _ in range(size)] for _ in range(size)]
    return res


def det(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    result = 0
    for i in range(len(m)):
        result += math.pow(-1, i)*m[0][i]*det(create_minor(m, i))
    return result


def create_minor(m, index):
    assert index < len(m)
    minor = copy.deepcopy(m)
    del minor[0]
    for i in minor:
        del i[index]
    return minor


def print_matrix(print_me):
    for i in range(len(print_me)):
        print(print_me[i])
    print("\n")


matrix = generate_matrix(8)
print_matrix(matrix)
print(det(matrix))

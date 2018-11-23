
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

if len(a) != len(b):
    print("Vectors need to be same length")
    exit()

result = 0
for i in range(len(a)):
    result += a[i]*b[i]
print(result)

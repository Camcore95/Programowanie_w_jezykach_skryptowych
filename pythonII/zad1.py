import sys

input = open("input.txt", "r")
output = open("output.txt", "w")
sys.stdout = output

for line in input:
    print(line, end='')

input.close()
output.close()

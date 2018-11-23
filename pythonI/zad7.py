import sys
import math

if len(sys.argv) != 4:
    exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(b*b-4*a*c)

if d == 0:
    x0 = -b/(2*a)
    print("x0= ", x0)
elif d > 0:
    d = math.sqrt(d)
    x1 = (-b-d)/(2*a)
    x2 = (-b+d)/(2*a)
    print("x1= ", x1, ", x2=", x2)
else:
    print("No answer in real domain")


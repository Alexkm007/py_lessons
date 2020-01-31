from math import sqrt
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c
if d > 0:
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    print(int(x1))
    print(int(x2))
elif d == 0:
    x = -b/(2*a)
    print(int(x))
else:
    print("ошибка нет решения")

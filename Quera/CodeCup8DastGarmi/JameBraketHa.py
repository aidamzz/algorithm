import math
n = int(input())
l = []
for i in range(n):
    m = int(input())
    x = float(input())
    l.append((m,x))

for (i, j) in l:
    print(math.floor(i*j))
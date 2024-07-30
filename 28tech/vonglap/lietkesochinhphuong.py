import math
n = int(input())
for i in range(1, int(math.sqrt(n)) + 1, 1):
    print(i * i, end=' ')

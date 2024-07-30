import math
n = int(input())
tong = 0
for i in range(1, n + 1, 1):
    tong += int(math.pow(-1, i) * i)
print(tong)

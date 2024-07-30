import math
n = int(input())
tong = 0
for i in range(1, int(math.sqrt(n)) + 1, 1):
    if (n % i == 0):
        tong += i
        if (n // i != i):
            tong += (n // i)
print(tong)

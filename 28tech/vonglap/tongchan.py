n = int(input())
tong = 0
for i in range(1, n + 1, 1):
    x = int(input())
    if (x % 2 == 0):
        tong += x
print(tong)

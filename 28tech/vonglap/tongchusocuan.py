n = int(input())
tong = 0
while (n):
    tong += int(n % 10)
    n //= 10
print(tong)

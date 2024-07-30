n = int(input())
tich = 1
for i in range(1, n + 1, 1):
    if (n % i == 0):
        tich *= i
print(tich)

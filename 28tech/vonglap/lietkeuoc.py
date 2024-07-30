n = int(input())
dem = 0
for i in range(1, n + 1, 1):
    if (n % i == 0):
        dem += 1
print(dem)
for i in range(1, n + 1, 1):
    if (n % i == 0):
        print(i, end=" ")

n = int(input())
dem = 0
while (n):
    m = n % 10
    if (m == 2 or m == 3 or m == 5 or m == 7):
        dem += 1
    n //= 10
print(dem)

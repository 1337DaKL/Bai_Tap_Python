n = int(input())
a = list(map(int, input().split()))
b = list()
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
        dem = 0
        for j in range(n):
            if a[i] == a[j]:
                dem += 1
        print(a[i], dem, sep=' ', end='\n')

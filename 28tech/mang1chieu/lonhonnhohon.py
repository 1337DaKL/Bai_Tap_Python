n = int(input())
a = list(map(int, input().split()))
m = int(input())
demlon, demnho = 0, 0
for i in range(0, len(a), 1):
    if a[i] > m:
        demlon += 1
    if (a[i] < m):
        demnho += 1
print(demnho, demlon, sep='\n')

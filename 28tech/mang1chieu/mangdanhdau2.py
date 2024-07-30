n = int(input())
a = list(map(int, input().split()))
b = [0] * 1000001
for i in range(0, n, 1):
    b[a[i]] += 1
a.sort()
for i in range(0, n, 1):
    if b[a[i]] != 0:
        print(a[i], b[a[i]], sep=' ', end='\n')
        b[a[i]] = 0

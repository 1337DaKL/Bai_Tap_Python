n = int(input())
a = list(map(int, input().split()))
b = [0] * 1000000
for i in range(0, n, 1):
    b[a[i]] += 1
maxo = 0
for i in range(n):
    maxo = max(maxo, b[a[i]])
a.sort()
for i in range(n):
    if b[a[i]] == maxo:
        print(a[i], b[a[i]], sep=' ', end='\n')
        break

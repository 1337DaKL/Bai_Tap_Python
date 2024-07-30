ok = 1000000000 + 7
n = int(input())
a = list(map(int, input().split()))
tong, tich = 0, 1
for i in range(n):
    tong = (tong % ok + a[i] % ok) % ok
    tich = (tich % ok * a[i] % ok) % ok
print(tong, tich, sep='\n')

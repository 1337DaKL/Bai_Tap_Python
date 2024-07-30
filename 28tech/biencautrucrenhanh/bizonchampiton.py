a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())
tonga = a1 + a2 + a3
tongb = b1 + b2 + b3
tongke = 0
if tonga % 5 == 0:
    tongke += (tonga // 5)
else:
    tongke += (tonga // 5 + 1)
if tongb % 10 == 0:
    tongke += (tongb // 10)
else:
    tongke += (tongb // 10 + 1)
if tongke <= n:
    print("YES")
else:
    print("NO")

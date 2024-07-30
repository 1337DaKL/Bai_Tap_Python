a, b, c, n = map(int, input().split())
tong = a + b + c + n
if tong % 3 != 0:
    print("NO")
else:
    deu = tong // 3
    if deu >= a and deu >= b and deu >= c:
        print("YES")
    else:
        print("NO")

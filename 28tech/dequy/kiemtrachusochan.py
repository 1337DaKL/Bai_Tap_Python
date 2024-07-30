def check(n):
    if (n == 0):
        return True
    m = n % 10
    if (m % 2 == 1):
        return False
    else:
        return check(n // 10)


if __name__ == '__main__':
    n = int(input())
    if (check(n)):
        print("YES")
    else:
        print("NO")

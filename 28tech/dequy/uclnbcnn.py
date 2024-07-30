def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)


def bcnn(a, b):
    c = ucln(a, b)
    return (a * b) // c


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(ucln(n, m), bcnn(n, m), sep=' ', end='')

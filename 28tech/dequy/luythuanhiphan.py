ok = 1000000000 + 7


def luythua(a, b):
    if (b == 0):
        return 1
    pin = luythua(a, b // 2)
    if (b % 2 == 0):
        return (pin % ok * pin % ok) % ok
    else:
        return (pin % ok * (pin % ok * a % ok) % ok) % ok


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(luythua(a, b))

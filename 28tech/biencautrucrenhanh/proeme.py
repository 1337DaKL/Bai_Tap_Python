import math
a, b, c = map(float, input().split())
if (a == 0 and b == 0 and c == 0):
    print("VO SO NGHIEM")
elif a == 0:
    print('%.2f' % (-c / b))
elif a != 0:
    deta = b * b - 4 * a * c
    if deta < 0:
        print("VO NGHIEM")
    elif (deta == 0):
        x = - b / (2 * a)
        print('%.2f' % x)
    else:
        x1 = (-b - math.sqrt(deta)) / (2 * a)
        x2 = (-b + math.sqrt(deta)) / (2 * a)
        print('%.2f' % x1, '%.2f' % x2, sep=" ")

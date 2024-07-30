a = input()
if a == 'z' or a == 'Z':
    print('a')
elif a >= 'a' and a < 'z':
    b = int(ord(a)) + 1
    print(chr(b))
else:
    b = int(ord(a) + 33)
    print(chr(b))

c = input()
if c >= 'a' and c <= 'z':
    b = int(ord(c)) - 32
    print(chr(b))
elif c >= 'A' and c <= 'Z':
    b = int(ord(c)) + 32
    print(chr(b))
else:
    print(c)

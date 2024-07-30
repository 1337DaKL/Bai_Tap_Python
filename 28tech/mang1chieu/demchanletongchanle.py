n = int(input())
a = list(map(int, input().split()))
demle, demchan, tongle, tongchan = 0, 0, 0, 0
for i in range(0, len(a), 1):
    if a[i] % 2 == 0:
        demchan += 1
        tongchan += a[i]
    else:
        demle += 1
        tongle += a[i]
print(demchan, demle, tongchan, tongle, sep='\n')

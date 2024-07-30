n = int(input())
dem = n // 28
vo = n // 28
while (vo >= 3):
    dem += int(vo // 3)
    voconlai = (vo // 3) + (vo % 3)
    vo = voconlai
print(dem)

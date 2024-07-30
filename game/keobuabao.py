import pygame
from random import randint


def main():
    pygame.init()
    pygame.display.set_caption("Game_Keo_Bua_Bao_By_1337DaKL")

    icon = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\download (2).jpg')
    bgr = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\download.jpg')
    bgr = pygame.transform.scale2x(bgr)
    pygame.display.set_icon(icon)

    keo = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\OIP (1)(1).jpg')
    keo = pygame.transform.scale2x(keo)
    keo_hcn = keo.get_rect(center=(90, 100))
    keo_randoom = keo.get_rect(center=(900, 400))

    bua = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\OIP (2)(1).jpg')
    bua = pygame.transform.scale2x(bua)
    bua_hcn = bua.get_rect(center=(100, 300))
    bua_randoom = bua.get_rect(center=(900, 400))

    bao = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\th(1).jpg')
    bao = pygame.transform.scale2x(bao)
    bao_hcn = bao.get_rect(center=(100, 500))
    bao_randoom = bao.get_rect(center=(900, 400))

    screen = pygame.display.set_mode((1000, 700))

    you_win = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\th (1).jpg')
    you_win = pygame.transform.scale2x(you_win)
    you_win_hcn = you_win.get_rect(center=(500, 350))

    you_lose = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\download (3).jpg')
    you_lose = pygame.transform.scale2x(you_lose)
    you_lose_hcn = you_lose.get_rect(center=(500, 350))

    hoa = pygame.image.load(
        r'C:\Users\luong\OneDrive\Documents\baitappython\game\images\OIP (3)(1).jpg')
    hoa = pygame.transform.scale2x(hoa)
    hoa_hcn = hoa.get_rect(center=(500, 350))

    running = True
    check = 0
    check_computer = 8

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    check = 1
                elif event.key == pygame.K_2:
                    check = 2
                elif event.key == pygame.K_3:
                    check = 3

                check_computer = randint(1, 3)

        screen.blit(bgr, (0, 0))
        screen.blit(keo, keo_hcn)
        screen.blit(bua, bua_hcn)
        screen.blit(bao, bao_hcn)

        if check:
            if check_computer == 1:
                screen.blit(keo, keo_randoom)
            elif check_computer == 2:
                screen.blit(bua, bua_randoom)
            else:
                screen.blit(bao, bao_randoom)

            if check == 1:
                if check_computer == 3:
                    screen.blit(you_win, you_win_hcn)
                elif check_computer == 2:
                    screen.blit(you_lose, you_lose_hcn)
                else:
                    screen.blit(hoa, hoa_hcn)
            elif check == 2:
                if check_computer == 1:
                    screen.blit(you_win, you_win_hcn)
                elif check_computer == 3:
                    screen.blit(you_lose, you_lose_hcn)
                else:
                    screen.blit(hoa, hoa_hcn)
            elif check == 3:
                if check_computer == 2:
                    screen.blit(you_win, you_win_hcn)
                elif check_computer == 1:
                    screen.blit(you_lose, you_lose_hcn)
                else:
                    screen.blit(hoa, hoa_hcn)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

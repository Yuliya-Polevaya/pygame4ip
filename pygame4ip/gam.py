# import sys
# import pygame
#
#
# pygame.init()
#
# W = 900
# H = 600
#
# sc = pygame.display.set_mode((W, H))
# pygame.display.set_caption("События от клавиатуры")
# #pygame.display.set_icon(pygame.image.load("app.bmp"))
#
# WHITE = (233,154,183)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# FPS = 60  # число кадров в секунду
# clock = pygame.time.Clock()
#
# SIZE = 100
# player_img = pygame.image.load("player2.jpg").convert_alpha()
# player_img = pygame.transform.scale(player_img, (SIZE, SIZE))
#
# x = W // 2
# y = H // 2
# speed = 10
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 x -= speed
#             elif event.key == pygame.K_d:
#                 x += speed
#
#             elif event.key == pygame.K_w:
#                 y -= speed
#
#             elif event.key == pygame.K_s:
#                 y += speed
#
#             elif event.key == pygame.K_q:
#                 y -= speed
#                 x -= speed
#
#             elif event.key == pygame.K_e:
#                 y -= speed
#                 x += speed
#
#             elif event.key == pygame.K_z:
#                 y += speed
#                 x -= speed
#
#             elif event.key == pygame.K_x:
#                 y += speed
#                 x += speed
#
#
#     sc.fill(WHITE)
#     sc.blit(player_img, (x, y))
#     pygame.display.update()
#
#     clock.tick(FPS)


import pygame
import sys
import cv2
import numpy as np

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
WHITE = (0,0,0)
BLACK = (107, 247, 228)
RED = (247, 82, 159)
crosses = []
circles = []
current_player = "cross"

while True:
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (130, 130, 234, 234))

    buttons = [
        pygame.draw.rect(screen, RED, (140, 140, 70, 70)),
        pygame.draw.rect(screen, RED, (212, 140, 70, 70)),
        pygame.draw.rect(screen, RED, (284, 140, 70, 70)),
        pygame.draw.rect(screen, RED, (140, 212, 70, 70)),
        pygame.draw.rect(screen, RED, (212, 212, 70, 70)),
        pygame.draw.rect(screen, RED, (284, 212, 70, 70)),
        pygame.draw.rect(screen, RED, (140, 284, 70, 70)),
        pygame.draw.rect(screen, RED, (212, 284, 70, 70)),
        pygame.draw.rect(screen, RED, (284, 284, 70, 70)),
    ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos) and i not in crosses and i not in circles:
                    if current_player == "cross":
                        crosses.append(i)
                        current_player = "circle"
                    else:
                        circles.append(i)
                        current_player = "cross"
                    break

    for i in crosses:
        button = buttons[i]
        pygame.draw.line(screen, (227,233,119),
                         button.topleft, button.bottomright, 3)
        pygame.draw.line(screen, (227,233,119),
                         button.topright, button.bottomleft, 3)

    for i in circles:
        button = buttons[i]
        center = button.center
        radius = 25
        pygame.draw.circle(screen, (126,233,110), center, radius, 3)

    pygame.display.flip()
    clock.tick(60)
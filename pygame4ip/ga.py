import pygame
import sys
import cv2
import numpy as np

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
WHITE = (0,0,0)
BLACK = (232,233,187)
RED = (233,196,221)
font_small = pygame.font.Font(None, 36)
player_image = pygame.image.load('Enemy.jpg').convert_alpha()
player_image = pygame.transform.scale(player_image, (140, 140))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)
    pole = pygame.draw.rect(screen, BLACK, (30, 30, 450, 450))
    pygame.draw.rect(screen, RED, (36, 180, 140, 140))
    pygame.draw.rect(screen, RED, (185, 180, 140, 140))
    pygame.draw.rect(screen, RED, (334, 180, 140, 140))

    score_text = font_small.render(f"Найди кота", True, WHITE)
    screen.blit(score_text, (185, 70))


    pygame.display.flip()
    clock.tick(60)
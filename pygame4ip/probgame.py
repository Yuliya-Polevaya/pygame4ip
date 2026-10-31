# Импортируем библиотеки
import pygame, sys
from pygame.locals import *
import random

# Инициализируем Pygame
pygame.init()

# Ограничиваем количество кадров в секунду
FPS = 60
FramePerSec = pygame.time.Clock()

# Задаем цвет
WHITE = (255, 255, 255)

# Задаем размеры игрового экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Отрисовываем экран и заливаем его белым цветом
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Определяем класс игрока


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # Определяем класс врага


class Enemy(pygame.sprite.Sprite):
    def __init__(self ) :
        super().__init__()
        self.image = pygame.image.load("Enemy.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # Создаем персонажей


P1 = Player()
E1 = Enemy()

# Определяем игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
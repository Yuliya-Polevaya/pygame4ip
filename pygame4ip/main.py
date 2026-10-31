import pygame
import sys
import cv2
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1200, 1000))
WHITE = (0,0,0)
BLACK = (107, 247, 228)
RED = (247, 82, 159)
BLUE = (84, 19, 247)
GREEN = (150, 247, 161)

font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()


HelloWorldColors = [BLACK, RED, BLUE, GREEN]

# Загрузка видео
VIDEO_FILES = ["video.mp4","video2.mp4","video3.mp4","video4.mp4","video5.mp4","video6.mp4"]
video_index = 0
cap = cv2.VideoCapture(VIDEO_FILES[video_index])

# Позиции
text_pos = [400, 400]      # центр текста
video_pos = [200, 100]     # левый верхний угол видео
VIDEO_W, VIDEO_H = 400, 550
VIDEO_SPEED = 10           # пиксели за один кадр при зажатой стрелке

count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            text_pos = list(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            # переключение видео по пробелу
            if event.key == pygame.K_SPACE:
                cap.release()
                video_index = (video_index + 1) % len(VIDEO_FILES)
                cap = cv2.VideoCapture(VIDEO_FILES[video_index])

    if not running:
        break

    # перемещение видео стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        video_pos[0] -= VIDEO_SPEED
    if keys[pygame.K_RIGHT]:
        video_pos[0] += VIDEO_SPEED
    if keys[pygame.K_UP]:
        video_pos[1] -= VIDEO_SPEED
    if keys[pygame.K_DOWN]:
        video_pos[1] += VIDEO_SPEED

    # чтобы видео не уезжало за экран
    video_pos[0] = max(0, min(video_pos[0], screen.get_width() - VIDEO_W))
    video_pos[1] = max(0, min(video_pos[1], screen.get_height() - VIDEO_H))

    count += 1
    screen.fill(WHITE)

    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (VIDEO_W, VIDEO_H))
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(frame_surface, video_pos)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # текст
    text = font.render("Hello World", True, HelloWorldColors[count % 4])
    text_rect = text.get_rect(center=text_pos)
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
sys.exit()
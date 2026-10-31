import pygame
import sys

# Инициализация
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders: Большой НЛО")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHT_GREEN = (0, 255, 0)

# Шрифты
font_size = 48
font = pygame.font.Font(None, font_size)
font_small = pygame.font.Font(None, 36)

# Загрузка вашего изображения для НЛО
# Убедитесь, что файл 'your_image.png' находится в той же папке
player_image = pygame.image.load('your_image.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (200, 200))  # подгоните размер по необходимости

# Загрузка вашего изображения для игрока
# Замените 'your_photo.png' на путь к вашему фото
player_photo = pygame.image.load('your_photo.jpg').convert_alpha()
player_photo = pygame.transform.scale(player_photo, (200, 200))  # подгоните размер


# Класс НЛО
class SaucerSprite:
    def __init__(self, x, y, scale=2):
        self.image = player_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.dead = False
        self.points = 300
        self.score_surface = font.render(str(self.points), True, WHITE)
        self.show_score_time = 300  # быстрее появление
        self.death_time = 0

    def move_left(self):
        if not self.dead:
            self.rect.x -= self.speed

    def move_right(self):
        if not self.dead:
            self.rect.x += self.speed

    def draw(self, surface):
        if self.dead:
            surface.blit(self.score_surface, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def update(self):
        if self.rect.right < 0:
            self.dead = True
            self.death_time = pygame.time.get_ticks()

    def kill(self):
        if not self.dead:
            self.dead = True
            self.death_time = pygame.time.get_ticks()

    def is_hit(self, bullet_rect):
        return self.rect.colliderect(bullet_rect)

# Пуля
class Bullet:
    def __init__(self, x, y):
        self.width = 5
        self.height = 15
        self.color = WHITE
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = -7
        self.active = True

    def move(self):
        if self.active:
            self.rect.y += self.speed
            if self.rect.bottom < 0:
                self.active = False

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect)

def main():
    clock = pygame.time.Clock()
    score = 0

    # Создаем НЛО
    saucer = SaucerSprite(WIDTH, 50, scale=2.5)

    # Пуля
    bullet = None

    # Управление игроком
    player_x = WIDTH // 2
    player_speed = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление стрелками
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            if player_x < 0:
                player_x = 0
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            if player_x > WIDTH:
                player_x = WIDTH

        # Стрельба
        if keys[pygame.K_SPACE]:
            if not bullet or not bullet.active:
                bullet_x = player_x
                bullet_y = HEIGHT - 50
                bullet = Bullet(bullet_x, bullet_y)

        # Движение НЛО
        if not saucer.dead:
            saucer.move_left()
            saucer.update()

        # Движение пули
        if bullet and bullet.active:
            bullet.move()

        # Проверка попадания
        if not saucer.dead and bullet and bullet.active:
            if saucer.is_hit(bullet.rect):
                saucer.kill()
                score += saucer.points
                saucer.show_score_time = 300  # Меньше задержки для повторного появления
                saucer.death_time = pygame.time.get_ticks()

        # Время отображения очков
        if saucer.dead:
            current_time = pygame.time.get_ticks()
            if current_time - saucer.death_time > saucer.show_score_time:
                # после показа очков создаем нового НЛО
                saucer = SaucerSprite(WIDTH, 50, scale=2.5)

        # Очистка экрана
        window.fill(BLACK)

        # Рисуем НЛО
        saucer.draw(window)

        # Рисуем пулю
        if bullet and bullet.active:
            bullet.draw(window)

        # Рисуем ваше фото
        player_rect = player_photo.get_rect(center=(player_x, HEIGHT - 20))
        window.blit(player_photo, player_rect)

        # Отображение очков
        score_text = font_small.render(f"Очки: {score}", True, WHITE)
        window.blit(score_text, (10, 10))


        pygame.display.flip()
        clock.tick(100)

if __name__ == "__main__":
    main()
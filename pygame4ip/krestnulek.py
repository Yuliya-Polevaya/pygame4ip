import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = WIDTH // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики на двоих")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (247, 82, 159)
BLUE  = (191,57,244)

font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# --- состояние игры ---
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

current_player = 'X'   # чей сейчас ход
game_over = False
winner = None


def reset_game():
    """Сброс доски — X ходит первым."""
    global board, current_player, game_over, winner
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    current_player = 'X'
    game_over = False
    winner = None


def draw_the_board():
    screen.fill(WHITE)
    # линии сетки
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * CELL, 0), (i * CELL, HEIGHT), 4)
        pygame.draw.line(screen, BLACK, (0, i * CELL), (WIDTH, i * CELL), 4)
    # символы
    for r in range(3):
        for c in range(3):
            if board[r][c]:
                color = RED if board[r][c] == 'X' else BLUE
                text = font.render(board[r][c], True, color)
                rect = text.get_rect(center=(c * CELL + CELL // 2,
                                             r * CELL + CELL // 2))
                screen.blit(text, rect)

    # чей ход
    if not game_over:
        turn = small_font.render(f"Ход: {current_player}", True, BLACK)
        turn_rect = turn.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(turn, turn_rect)


def check_if_anyone_won():
    # строки
    for r in range(3):
        if board[r][0] and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # столбцы
    for c in range(3):
        if board[0][c] and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # диагонали
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def check_for_win_or_draw():
    global winner, game_over
    w = check_if_anyone_won()
    if w:
        winner = w
        game_over = True
        return True
    # ничья: все клетки заняты
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                return False
    winner = 'Ничья'
    game_over = True
    return True


def run_event_processing():
    """Обработка кликов и клавиш. Ходы делает тот, чья очередь."""
    global current_player, game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # рестарт без перезапуска программы
            if event.key == pygame.K_r:
                reset_game()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = pygame.mouse.get_pos()
            c = mx // CELL
            r = my // CELL
            if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == '':
                board[r][c] = current_player

                if check_for_win_or_draw():
                    return

                # передаём ход другому игроку
                current_player = 'O' if current_player == 'X' else 'X'


def draw_game_over_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(WHITE)
    screen.blit(overlay, (0, 0))

    if winner == 'Ничья':
        msg = "Ничья!"
    else:
        msg = f"{winner} победил!"

    text = font.render(msg, True, BLACK)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, rect)

    hint = small_font.render("Нажми R для новой игры", True, BLACK)
    hint_rect = hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    screen.blit(hint, hint_rect)


# --- старт партии ---
reset_game()

# --- основной игровой цикл ---
while True:
    run_event_processing()

    draw_the_board()

    if game_over:
        draw_game_over_screen()

    pygame.display.flip()
    clock.tick(60)
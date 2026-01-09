import pygame
import random
import sys

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 360, 420
GRID_SIZE = 3
TILE_SIZE = 120

BG_COLOR = (30, 30, 30)
TILE_COLOR = (76, 175, 80)
EMPTY_COLOR = (200, 200, 200)
TEXT_COLOR = (255, 255, 255)

GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = {
    pygame.K_UP: (-1, 0),
    pygame.K_DOWN: (1, 0),
    pygame.K_LEFT: (0, -1),
    pygame.K_RIGHT: (0, 1)
}

# ---------------- UTILITY ----------------
def is_solvable(state):
    arr = [n for row in state for n in row if n != 0]
    inv = sum(arr[i] > arr[j] for i in range(len(arr)) for j in range(i+1, len(arr)))
    return inv % 2 == 0

def generate_board():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        board = tuple(tuple(nums[i*3:(i+1)*3]) for i in range(3))
        if is_solvable(board) and board != GOAL:
            return board

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def swap(board, x1, y1, x2, y2):
    b = [list(r) for r in board]
    b[x1][y1], b[x2][y2] = b[x2][y2], b[x1][y1]
    return tuple(tuple(r) for r in b)

# ---------------- GAME ----------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8 Puzzle Game")
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    board = generate_board()
    moves = 0

    def draw():
        screen.fill(BG_COLOR)

        for i in range(3):
            for j in range(3):
                val = board[i][j]
                x, y = j * TILE_SIZE, i * TILE_SIZE

                color = TILE_COLOR if val != 0 else EMPTY_COLOR
                pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (0,0,0), (x, y, TILE_SIZE, TILE_SIZE), 2)

                if val != 0:
                    text = font.render(str(val), True, TEXT_COLOR)
                    rect = text.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                    screen.blit(text, rect)

        info = small_font.render(f"Moves: {moves} | R=Restart  ESC=Quit", True, TEXT_COLOR)
        screen.blit(info, (10, 370))

        if board == GOAL:
            win = font.render("SOLVED!", True, (255, 215, 0))
            screen.blit(win, (100, 180))

        pygame.display.flip()

    running = True
    while running:
        draw()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r:
                    board = generate_board()
                    moves = 0

                elif event.key in MOVES:
                    zx, zy = find_zero(board)
                    dx, dy = MOVES[event.key]
                    nx, ny = zx + dx, zy + dy
                    if 0 <= nx < 3 and 0 <= ny < 3:
                        board = swap(board, zx, zy, nx, ny)
                        moves += 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                j, i = mx // TILE_SIZE, my // TILE_SIZE
                if 0 <= i < 3 and 0 <= j < 3:
                    zx, zy = find_zero(board)
                    if abs(zx - i) + abs(zy - j) == 1:
                        board = swap(board, zx, zy, i, j)
                        moves += 1

    pygame.quit()
    sys.exit()

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()

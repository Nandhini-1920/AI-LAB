import pygame
from collections import deque
import sys
import time

pygame.init()

# ---------------- SETTINGS ----------------
CELL = 60
maze = [
    list("S000100000"),
    list("1110101110"),
    list("0000100000"),
    list("0111101110"),
    list("0000000010"),
    list("0111111010"),
    list("0100000010"),
    list("0101111110"),
    list("0000000000"),
    list("011111111G")
]

ROWS, COLS = len(maze), len(maze[0])
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game – Human vs AI")

# ---------------- COLORS ----------------
WHITE = (245,245,245)
BLACK = (20,20,20)
GREEN = (0,200,0)    # human
RED = (220,0,0)      # goal
BLUE = (0,120,255)   # AI
GRAY = (180,180,180)

FONT_BIG = pygame.font.SysFont(None, 60)
FONT_SMALL = pygame.font.SysFont(None, 28)

MOVES = [(0,1),(1,0),(0,-1),(-1,0)]

# ---------------- HELPERS ----------------
def find_pos(symbol):
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == symbol:
                return (i, j)

start = find_pos('S')
goal = find_pos('G')

player = start
ai = start

def valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] != '1'

# ---------------- BFS (AI) ----------------
def bfs(start):
    q = deque([(start, [start])])
    visited = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for dx, dy in MOVES:
            nx, ny = node[0]+dx, node[1]+dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), path+[(nx, ny)]))

ai_path = bfs(ai)
ai_index = 0

# ---------------- DRAW ----------------
def draw():
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j*CELL, i*CELL, CELL, CELL)
            if maze[i][j] == '1':
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

    # Draw goal
    gx, gy = goal
    pygame.draw.rect(screen, RED, (gy*CELL, gx*CELL, CELL, CELL))

    # Draw AI
    ax, ay = ai
    pygame.draw.rect(screen, BLUE, (ay*CELL, ax*CELL, CELL, CELL))

    # Draw player
    px, py = player
    pygame.draw.rect(screen, GREEN, (py*CELL, px*CELL, CELL, CELL))

# ---------------- END SCREEN ----------------
def end_screen(text, color):
    screen.fill(WHITE)
    msg = FONT_BIG.render(text, True, color)
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 30))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# ---------------- START SCREEN ----------------
def start_screen():
    while True:
        screen.fill(WHITE)
        title = FONT_BIG.render("HUMAN vs AI MAZE", True, BLACK)
        info = FONT_SMALL.render("Reach the goal before the AI", True, BLACK)
        start_msg = FONT_SMALL.render("Press ENTER to start", True, BLACK)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))
        screen.blit(info, (WIDTH//2 - info.get_width()//2, 280))
        screen.blit(start_msg, (WIDTH//2 - start_msg.get_width()//2, 340))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

# ---------------- GAME LOOP ----------------
start_screen()
clock = pygame.time.Clock()
ai_timer = 0

while True:
    clock.tick(60)
    screen.fill(WHITE)
    draw()
    pygame.display.flip()

    # ---- AI MOVE every 0.5 sec ----
    ai_timer += clock.get_time()
    if ai_timer > 500 and ai_index < len(ai_path)-1:
        ai_index += 1
        ai = ai_path[ai_index]
        ai_timer = 0

    # ---- WIN CHECK ----
    if ai == goal:
        end_screen("AI WINS!", BLUE)
    if player == goal:
        end_screen("YOU WIN!", GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x, y = player
            if event.key in [pygame.K_UP, pygame.K_w] and valid(x-1,y):
                player = (x-1,y)
            if event.key in [pygame.K_DOWN, pygame.K_s] and valid(x+1,y):
                player = (x+1,y)
            if event.key in [pygame.K_LEFT, pygame.K_a] and valid(x,y-1):
                player = (x,y-1)
            if event.key in [pygame.K_RIGHT, pygame.K_d] and valid(x,y+1):
                player = (x,y+1)


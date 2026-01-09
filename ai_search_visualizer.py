import pygame
import sys
import time
from collections import deque

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Search Visualizer – BFS & DFS")

FONT_BIG = pygame.font.SysFont("arial", 40, bold=True)
FONT = pygame.font.SysFont("arial", 22)
FONT_SMALL = pygame.font.SysFont("arial", 18)

# ---------------- COLORS ----------------
BG_TOP = (30, 40, 60)
BG_BOTTOM = (15, 20, 30)
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (90, 150, 255)
GREEN = (0, 200, 120)
GRAY = (170, 170, 170)
RED = (240, 80, 80)
PANEL = (40, 55, 80)

# ---------------- GRAPH ----------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

positions = {
    'A': (450, 100),
    'B': (250, 220),
    'C': (650, 220),
    'D': (180, 340),
    'E': (320, 340),
    'F': (580, 340),
    'G': (720, 340),
    'H': (180, 460),
    'I': (320, 460),
    'J': (720, 460)
}

start_node = 'A'
target_node = 'J'
visited = set()

# ---------------- PRE-RENDER BACKGROUND ----------------
background = pygame.Surface((WIDTH, HEIGHT))
for y in range(HEIGHT):
    ratio = y / HEIGHT
    r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
    g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
    b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
    pygame.draw.line(background, (r, g, b), (0, y), (WIDTH, y))

# ---------------- DRAW GRAPH ----------------
def draw_graph(active=None):
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, 90))

    title = FONT_BIG.render("AI SEARCH VISUALIZER", True, WHITE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 22))

    info = FONT.render("1: BFS   2: DFS   3: Exit", True, WHITE)
    screen.blit(info, (20, 35))

    legend = FONT_SMALL.render(f"Start: {start_node}    Target: {target_node}", True, WHITE)
    screen.blit(legend, (WIDTH - 260, 38))

    # Draw edges
    for node in graph:
        for n in graph[node]:
            pygame.draw.line(screen, GRAY, positions[node], positions[n], 2)

    # Draw nodes
    for node, pos in positions.items():
        if node == target_node:
            color = RED
        elif node in visited:
            color = GREEN
        else:
            color = BLUE

        if node == active:
            pygame.draw.circle(screen, WHITE, pos, 32)

        pygame.draw.circle(screen, color, pos, 26)
        pygame.draw.circle(screen, BLACK, pos, 26, 2)

        label = FONT.render(node, True, WHITE)
        screen.blit(label, (pos[0] - 8, pos[1] - 12))

    pygame.display.flip()

# ---------------- POPUP ----------------
def popup(message, color):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    box = pygame.Rect(WIDTH//2 - 230, HEIGHT//2 - 120, 460, 200)
    pygame.draw.rect(screen, WHITE, box, border_radius=14)

    text = FONT_BIG.render(message, True, color)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))

    pygame.display.flip()
    time.sleep(2)

# ---------------- BFS ----------------
def bfs(start):
    visited.clear()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            draw_graph(node)
            time.sleep(0.6)

            if node == target_node:
                popup("TARGET FOUND (BFS)", GREEN)
                return

            for n in graph[node]:
                if n not in visited:
                    queue.append(n)

    popup("TARGET NOT FOUND (BFS)", RED)

# ---------------- DFS ----------------
def dfs(node):
    visited.add(node)
    draw_graph(node)
    time.sleep(0.6)

    if node == target_node:
        return True

    for n in graph[node]:
        if n not in visited:
            if dfs(n):
                return True
    return False

# ---------------- MENU ----------------
def menu():
    clock = pygame.time.Clock()

    while True:
        draw_graph()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bfs(start_node)
                    visited.clear()

                if event.key == pygame.K_2:
                    visited.clear()
                    found = dfs(start_node)
                    popup("TARGET FOUND (DFS)" if found else "TARGET NOT FOUND (DFS)",
                          GREEN if found else RED)
                    visited.clear()

                if event.key == pygame.K_3 or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# ---------------- RUN ----------------
menu()

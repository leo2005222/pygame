# py mine sweeper
# py_ms_02.py

# 02. 폭탄 생성 및 그리기

import pygame
from random import randint

# 파이게임 초기화
pygame.init()

# 변수 초기화
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
GRAY_LINE = (100, 100, 100)
GRAY_TILE = (200, 200, 200)
YELLOW_BOMB = (255, 255, 0)
BLACK = (0, 0, 0)
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2

# 화면 생성
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('py mine sweeper')

# 게임 보드(필드) 생성
field = [[0 for _ in range(COL_COUNT)]for _ in range(ROW_COUNT)]

# 필그에 폭탄 생성하기
count = 0
while count < NUM_OF_BOMBS:
    xpos = randint(0, COL_COUNT - 1)
    ypos = randint(0, ROW_COUNT - 1)
    if field[ypos][xpos] == EMPTY:
        field[ypos][xpos] = BOMB
        count += 1

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 검정색 채우기
    screen.fill(BLACK)

    # 필드 그리기 (빈칸이면 회색(GRAY_TILE) 타일 그리기, 폭탄은 (YELLOW_BOMB) 타원그리기)
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            tile = field[y][x]
            tile_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if tile == EMPTY:
                pygame.draw.rect(screen, GRAY_TILE, tile_rect)
            elif tile == BOMB:
                pygame.draw.ellipse(screen, YELLOW_BOMB, tile_rect)

    # 격자 그리기
    for x in range(COL_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (x*CELL_SIZE, 0), (x*CELL_SIZE, ROW_COUNT*CELL_SIZE))
    for y in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (0, y*CELL_SIZE), (COL_COUNT*CELL_SIZE, y*CELL_SIZE))

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()

# py mine sweeper
# py_ms_04.py

# 04. 타일 클릭 처리 - 폭탄 주변 탐색 및 오픈

import pygame
from random import randint

# 파이게임 초기화
pygame.init()

# 환경 변수 초기화
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
NUM_OF_BOMBS = 20
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)

# 타일 상태 변수
EMPTY = 0
BOMB = 1
OPENED = 2

# 색상 변수
BLACK = (0, 0, 0)
GRAY_LINE = (100, 100, 100)
GRAY_TILE = (200, 200, 200)
YELLOW_BOMB = (255, 255, 0)

# 게임 오버 초기화
game_over = False

# 필드 초기화
field = [[EMPTY for _ in range(COL_COUNT)]for _ in range(ROW_COUNT)]

# 폭탄 필드에 추가하기
bomb_cnt = 0
while bomb_cnt < NUM_OF_BOMBS:
    bomb_x = randint(0, COL_COUNT - 1)
    bomb_y = randint(0, ROW_COUNT - 1)
    if field[bomb_y][bomb_x] == EMPTY:
        field[bomb_y][bomb_x] = BOMB
        bomb_cnt = bomb_cnt + 1  # bomb_cnt += 1

# 화면 생성
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('py minesweeper')

# 폭탄 개수 반환
def num_of_bomb(field, x_pos, y_pos):
    pass

# 타일 - 재귀 함수
def open_tile(field, x_pos, y_pos):
    pass

running = True
# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0] // CELL_SIZE
                y = event.pos[1] // CELL_SIZE
                if field[y][x] == BOMB:
                    game_over = True
                else:
                    print("타일 열기")

    # 화면 초기화
    screen.fill(BLACK)

    # 타일 그리기
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            tile = field[y][x]
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if tile == EMPTY or tile == BOMB:
                pygame.draw.rect(screen, GRAY_TILE, rect)

    # 격자 그리기
    for x in range(COL_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (x * CELL_SIZE, 0), (x * CELL_SIZE, ROW_COUNT * CELL_SIZE))
    for y in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (0, y * CELL_SIZE), (COL_COUNT * CELL_SIZE, y * CELL_SIZE))

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()

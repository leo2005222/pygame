# p_snake04_movesnake.py
# 뱀 이동하기

import pygame
import random

# 화면 초기화
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 변수 초기화
# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 셀 변수 설정
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH//CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT//CELL_SIZE

# 방향 변수
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction=DOWN

# 뱀 좌표 리스트
center_pos = (COL_COUNT//2, ROW_COUNT//2)
bodies = [center_pos]

# 먹이 10개 좌표 리스트
foods = []
for _ in range(10):
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

# 게임루프
while True:
    # 키 입력 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # 키 방향 설정
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        elif event.key == pygame.K_UP:
            direction = UP
        elif event.key == pygame.K_RIGHT:
            direction = RIGHT
        elif event.key == pygame.K_DOWN:
            direction = DOWN

    # 뱀 머리 추출하고 다음 방향으로 이동하기
    head = bodies[0]
    c_idx = head[0]
    r_idx = head[1]
    if direction == LEFT:
        c_idx -= 1
    elif direction == RIGHT:
        c_idx += 1
    elif direction == UP:
        r_idx -= 1
    elif direction == DOWN:
        r_idx += 1

    # 뱀 리스트에서 맨 앞에 이동좌표 추가
    b_pos = (c_idx, r_idx)
    bodies.insert(0, b_pos)

    # 뱀 꼬리 지우기
    bodies.pop()

    # 화면 처리
    screen.fill(BLACK)

    # 격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)

    # 먹이 그리기
    for one in foods:
        f_rect = (one[0]*CELL_SIZE, one[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, f_rect)

    # 뱀 그리기
    for one in bodies:
        b_rect = (one[0]*CELL_SIZE, one[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)

    # 화면 업데이트
    pygame.display.update()
    clock.tick(10)

# 게임종료
pygame.quit()

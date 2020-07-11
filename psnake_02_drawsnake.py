# psnake_02_drawsnake.py
# 뱀 몸통 그리기
# bodies[]: 뱀 좌표를 튜플로 보관하는 리스트
# bodies[(x1, y1), (x2, y2), ....]

import pygame

# 화면 설정하기
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")

# 변수 초기화
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 뱀 봐표 초기화
bodies = [(COL_COUNT//2, ROW_COUNT//2)]

# 게임 루프
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # 화면 그리기
    screen.fill(BLACK)
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx*CELL_SIZE, r_idx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)

    # 뱀 그리기
    for one in bodies:
        b_rect = (one[0]*CELL_SIZE, one[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)

    # 화면 업데이트
    pygame.display.update()

# 파이 게임 종료하기
pygame.quit()

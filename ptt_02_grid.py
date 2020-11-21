# ptt_02_grid.py
# 02. 격자 그리기

import pygame

# 파이게임 초기화
pygame.init()

# 변수 초기화
SCREEN_WIDTH = SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WHITE = (255, 255, 255)
CELL_SIZE = 150
COL_COUNT = SCREEN_WIDTH // 3
ROW_COUNT = SCREEN_HEIGHT // 3

# 파이게임 화면 초기화
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 사각형 그리기
    for y in range(COL_COUNT):
        for x in range(ROW_COUNT):
            one_rect = (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 1)

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()

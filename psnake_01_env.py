# psnake_01_env.py
# 게임 화면 설정하기
# 화면 크기:600x800
# 격자 간격:40px

import pygame

# 파이게임 초기화
pygame.init()

# 화면 설정: 창 만들기(캡션 만들기)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")

# 변수 초기화
GRAY = (120, 120, 120)
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 게임 루프
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # 화면 격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx*CELL_SIZE, r_idx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)

# 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()

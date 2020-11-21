# ptt_04_turn.py
# 04. 돌 놓기
import pygame

# 파이게임 초기화
pygame.init()

# 변수 초기화
SCREEN_WIDTH = SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
CELL_SIZE = 150
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
# board = [[0 for x in range(3)] for y in range(3)]
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# 게임 화면
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")


# 격자 그리기 함수 draw_grid()
def draw_grid():
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            one_rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 3)


# 셀 초인트를 보드 행열로 변환 함수 cell_to_board(tmpos)
def cell_to_board(t_pos):
    row = col = -1
    for y in range(ROW_COUNT):
        if y * CELL_SIZE <= t_pos[1] < y * CELL_SIZE + CELL_SIZE:
            row = y
    for x in range(COL_COUNT):
        if x * CELL_SIZE <= t_pos[0] < x * CELL_SIZE + CELL_SIZE:
            col = x
    return row, col


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                m_pos = pygame.mouse.get_pos()
                r, c = cell_to_board(m_pos)
                # print("{}행 {}열".format(r, c))
                board[r][c] = 'x'
                print(board)

    draw_grid()

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()

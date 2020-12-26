# ps_ms_05
# 마인스위퍼
# 05. 타일 클릭 처리

import pygame
from random import randint

# 파이게임 초기화
pygame.init()

# 화면 변수 초기화
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)

# 색상 변수
GRAY_LINE = (100, 100, 100)
GRAY_TILE = (200, 200, 200)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)

# 게임 변수
EMPTY = 0
BOMB = 1
OPENED = 2
NUM_OF_BOMBS = 20
GAME_OVER = False
OPEN_COUNT = 0
field = [[EMPTY for _ in range(COL_COUNT)]for _ in range(ROW_COUNT)]
checked = [[0for _ in range(COL_COUNT)]for _ in range(ROW_COUNT)]

# 글꼴 초기화
small_font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

message_clear = large_font.render('[ CLEARED ]', True, CYAN)
message_over = large_font.render('GAME OVER !', True, CYAN)
message_rect = message_clear.get_rect()
message_rect.center = (COL_COUNT * CELL_SIZE // 2, ROW_COUNT * CELL_SIZE // 2)

# 푝탄 생성
bomb_cnt = 0
while bomb_cnt < NUM_OF_BOMBS:
    b_x = randint(0, COL_COUNT - 1)
    b_y = randint(0, ROW_COUNT - 1)
    if field[b_y][b_x] == EMPTY:
        field[b_y][b_x] = BOMB
        bomb_cnt += 1

# 화면 생성
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PY Minesweeper')


# 폭탄 개수 구하기 num_of_bomb(x, y)
def num_of_bomb(tx, ty):
    b_count = 0
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            x_pos = tx + x_offset
            y_pos = ty + y_offset
            if 0 <= x_pos < COL_COUNT and 0 <= y_pos < ROW_COUNT:
                if field[y_pos][x_pos] == BOMB:
                    b_count += 1
    return b_count


# 오픈 타일 함수
def open_tile(tx, ty):
    global OPEN_COUNT
    if checked[ty][tx]:
        return
    checked[ty][tx] = True
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            x_pos = tx + x_offset
            y_pos = ty + y_offset
            if 0 <= x_pos < COL_COUNT and 0 <= y_pos < ROW_COUNT:
                if field[y_pos][x_pos] == EMPTY:
                    field[y_pos][x_pos] = OPENED
                    OPEN_COUNT += 1
                    b_count = num_of_bomb(x_pos, y_pos)
                    if b_count == 0 and not (x_pos == tx and y_pos == ty):
                        open_tile(x_pos, y_pos)


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0] // CELL_SIZE
                y = event.pos[1] // CELL_SIZE

                # 클릭 타일 표시
                rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (50, 50, 50), rect)
                pygame.display.update()
                pygame.time.delay(100)

                # 폭탄이면 게임오버 아니면 타일 오픈
                if field[y][x] == BOMB:
                    GAME_OVER = True
                elif field[y][x] == EMPTY:
                    # 타일 열기
                    open_tile(x, y)

    # 검정배경
    screen.fill(BLACK)

    # 필드 내용을 출력
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            one_rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY_TILE, one_rect)
            if field[y][x] == OPENED:
                pygame.draw.rect(screen, BLACK, one_rect)
                b_cnt = num_of_bomb(x, y)
                if b_cnt > 0:
                    # 폭탄 수를 출력
                    num_img = small_font.render('{}'.format(b_cnt), True, YELLOW)
                    screen.blit(num_img, (x * CELL_SIZE + CELL_SIZE // 5, y * CELL_SIZE + CELL_SIZE // 5))
            # 폭탄이면 타원 그리기
            if GAME_OVER and field[y][x] == BOMB:
                pygame.draw.ellipse(screen, YELLOW, one_rect)

    # 격자 그리기
    for x in range(COL_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (x * CELL_SIZE, 0), (x * CELL_SIZE, ROW_COUNT * CELL_SIZE))
    for y in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (0, y * CELL_SIZE), (COL_COUNT * CELL_SIZE, y * CELL_SIZE))

    # 메시지 출력하기
    if OPEN_COUNT == (COL_COUNT * ROW_COUNT - NUM_OF_BOMBS):
        screen.blit(message_clear, message_rect)
    elif GAME_OVER:
        screen.blit(message_over, message_rect)

    # 화면 갱신
    pygame.display.update()

# 파이게임 종료
pygame.quit()

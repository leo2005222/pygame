# ptt_05_making.py
#
import pygame

# 파이게임 초기화
pygame.init()

# 변수 초기화
SCREEN_WIDTH = SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
CELL_SIZE = 150
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE

# 화면 설정
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("파이틱택토")

# 보드 데이터
TTTData = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Turn = 'X'

# 돌 모양 설정하기
pygame.font.init()
turn_font = pygame.font.SysFont('arial black', 90)
result_font = pygame.font.SysFont('arial black', 70)
turn_x = turn_font.render('X', True, YELLOW)
turn_o = turn_font.render('O', True, YELLOW)
win_x = result_font.render('Winner X', True, WHITE)
win_o = result_font.render('Winner O', True, WHITE)


# 격자 그리기 함수
def draw_grid():
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            one_rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 3)
    # pygame.draw.rect(화면, 색상, 도형, 선 굵기)


# 클릭 좌표를 보드 인덱스로 변환
def cell_to_board(m_pos):
    for x in range(3):
        if CELL_SIZE * x < m_pos[0] <= CELL_SIZE * x + CELL_SIZE:
            cb_col = x
    for y in range(3):
        if CELL_SIZE * y < m_pos[1] <= CELL_SIZE * y + CELL_SIZE:
            cb_row = y
    return cb_row, cb_col


# 돌 모양 바꾸기
def change_turn():
    global Turn
    if Turn == 'X':
        Turn = 'O'
    else:
        Turn = 'X'


# 보드 그리기
def print_mark(p_row, p_col):
    turn_mark_rect = turn_o.get_rect().size
    p_x = p_col * CELL_SIZE + CELL_SIZE // 2 - turn_mark_rect[0] // 2
    p_y = p_row * CELL_SIZE + CELL_SIZE // 2 - turn_mark_rect[1] // 2
    if Turn == 'X':
        screen.blit(turn_x, (p_x, p_y))
    else:
        screen.blit(turn_o, (p_x, p_y))
    # TTTData 모든 값을 보드에 출력합니다.
    # screen.blit(turn_x, (x,y))


# 승자 판별하기
def check_winner(cw_row, cw_col):
    global running
    winner = False
    if TTTData[cw_row][0] == TTTData[cw_row][1] == TTTData[cw_row][2] == Turn:
        winner = True
    if TTTData[0][cw_col] == TTTData[1][cw_col] == TTTData[2][cw_col] == Turn:
        winner = True
    if cw_col - cw_row == 0:
        if TTTData[0][0] == TTTData[1][1] == TTTData[2][2]:
            winner = True
    if abs(cw_col - cw_row) == 2 or cw_col - cw_row == 0:
        if TTTData[0][2] == TTTData[1][1] == TTTData[2][0] == Turn:
            winner = True
    if winner:
        print(Turn, '승리')
        print_winner()
        running = False


def reset_data():
    global TTTData, Turn
    TTTData = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    Turn = 'X'
    screen.fill(BLACK)
    pygame.display.update()


# 승자 출력하기
def print_winner():
    # pygame은 RGBA(RED, GREEN, BLUE, ALPHA: 투명도) 지원하지 않는다
    # layer(surface) 생성 후 투명 이미지 출력
    result_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    result_surface.set_alpha(200)
    result_surface.fill(BLACK)
    screen.blit(result_surface, (0, 0))
    win_rect = win_o.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    if Turn == 'O':
        screen.blit(win_o, win_rect)
    else:
        screen.blit(win_x, win_rect)
    pygame.display.update()
    pygame.time.delay(2000)

    reset_data()
    py_main()


running = True


# 게임 루프
def py_main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = cell_to_board(mouse_pos)
                if TTTData[row][col] == 0:
                    TTTData[row][col] = Turn
                    print(TTTData)
                    print_mark(row, col)
                    check_winner(row, col)
                    change_turn()

        # 격자 그리기
        draw_grid()

        # 화면 업데이트
        pygame.display.update()

    # 파이게임 초기화
    pygame.quit()


py_main()

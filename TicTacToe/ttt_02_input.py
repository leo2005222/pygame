# ttt_02_input.py
# 틱택토 입력 받기


# 보드 출력 함수 선언
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-----")


# 변수 초기화
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# 보드 출력
prn_board(board)

# 입력 받기
for cnt in range(9):
    while True:
        y, x = map(int, input('y, x: ').split(','))
        # y, x 에 돌을 놓을 수 있는지 확인 후 가능하면 break
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")
    board[y][x] = 'x'
    prn_board(board)

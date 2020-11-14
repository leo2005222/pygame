# ttt_05_judge.py
# 틱택톡 대각선 판정


# 보드 출력 함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-"*5)


# 판정 함수 judge(y,x)
def judge(ty, tx):
    win = False
    if board[ty][0] == board[ty][1] == board[ty][2] == turn:
        win = True
    if board[0][tx] == board[1][tx] == board[2][tx] == turn:
        win = True
    if ty-tx == 0:
        if board[0][0] == board[1][1] == board[2][2] == turn:
            win = True
    if abs(ty-tx) == 2 or ty-tx == 0:
        if board[0][2] == board[1][1] == board[2][0] == turn:
            win = True
    return win


# 돌 변경
def change_stone(tt):
    if tt == 'X':
        return 'O'
    return 'X'


# 변수 초기화(board, turn)
msg = "DRAW"
turn = 'X'
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# 보드 출력
prn_board(board)

# 게임 루프
for x in range(9):
    while True:
        # 좌표 입력 받기
        y, x = map(int, input('%c 차례입니다. 위치를 지정해 주세요 y, x:' % turn).split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요")
    # 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 판정
    if judge(y, x):
        msg = turn + "의 승리!!!"
        break

    # 돌 모양 변경
    turn = change_stone(turn)

# 결과 출력
print(msg)

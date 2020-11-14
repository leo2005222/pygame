# ttt_03_turn.py
# 틱택토 돌 별로 입력받기


# 보드 출력 함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-"*5)


# 변수 초기화 (board 보드 데이터, turn 돌 모양(X, O))
turn = 'X'
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# 보드 출력
prn_board(board)

# 9회 동안 입력받기
for cnt in range(9):
    # 입력 좌표가 동일하면 재입력 받기
    while True:
        y, x = map(int, input('%c 차례입니다. 위치를 지정해 주세요 y, x:' % turn).split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요")

    # 좌표에 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 돌 모양 바꾸기
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

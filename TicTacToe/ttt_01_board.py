# ttt_01_board.py
# 틱택토 보드 출력


# 보드 출력 함수: def prn_board(board)
def prn_board(board):
    for r in range(3):
        print("{}|{}|{}|".format(board[r][0], board[r][1], board[r][2]))
        print("-----")


# 보드 초기화
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# 보드 출력
prn_board(board)

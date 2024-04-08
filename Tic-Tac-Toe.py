import random

#   보드판 출력 함수
def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r < 2:
            print("---|---|---")

#   승리 조건 확인 함수
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
            return True
        if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False
    
#   비김 조건 확인 함수
def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
    
#   게임 진행 함수
def tic_tac_toe():
    board = [[" " for i in range(3)] for j in range(3)] # 3x3 보드판 생성
    while True:
        print_board(board)
        x = int(input("다음 수의 x좌표를 입력하세요: ")) - 1
        y = int(input("다음 수의 y좌표를 입력하세요: ")) - 1
        if board[y][x] != " ":  # 이미 놓인 자리인 경우
            print("잘못된 위치입니다.")
            continue
        else:
            board[y][x] = 'X'
        if check_win(board):
            print_board(board)
            print("당신이 이겼습니다.")
            break

        if check_draw(board):
            print_board(board)
            print("비겼습니다.")
            break

        print("컴퓨터의 차례입니다.")
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[y][x] == " ":
                board[y][x] = 'O'
                if check_win(board):
                    print_board(board)
                    print("컴퓨터가 이겼습니다.")
                break
        
tic_tac_toe()
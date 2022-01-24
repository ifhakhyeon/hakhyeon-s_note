import sys
input = sys.stdin.readline

# 칸은 덮을 수 있는 네 가지 방법
cover_list = [[[0,0],[1,0],[0,1]],
              [[0,0],[0,1],[1,1]],
              [[0,0],[1,0],[1,1]],
              [[0,0],[1,0],[1,-1]]]

# delta로 덮는거(+1) 빼는거(-1) 컨트롤
def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        ny = y + cover_list[type][i][0]
        nx = x + cover_list[type][i][1]
        # len 을 쓰므로 out of range 주의
        if ny < 0 or ny > len(board)-1 or nx < 0 or nx > len(board[0])-1:
            ok = False

        elif (board[ny][nx] + delta) > 1:
            #이거 해줘야함
            board[ny][nx] += delta
            ok = False
        else:
            # 이거 해줘야함
            board[ny][nx] += delta
    return ok

def cover(board):
    y = -1
    x = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break

    if y == -1:
        return 1

    ret = 0
    for i in range(4):
        if set(board, y, x, i, 1):
            # print(board)
            ret += cover(board)
        set(board, y, x, i, -1)

    return ret

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        y, x = map(int, input().split())
        board_list = [[0 for _ in range(x)] for _ in range(y)]
        # print(board_list)
        cant = 0
        for i in range(y):
            line = input()
            for j in range(x):
                if line[j] == "#":
                    board_list[i][j] = 1
                else:
                    board_list[i][j] = 0
                    cant += 1
        # print(board_list)
        if cant % 3 != 0:
            print(0)
            continue

        print(cover(board_list))
import sys
input = sys.stdin.readline


# board = [
#     [2, 5, 1, 6, 1, 4, 1],
#     [6, 1, 1, 2, 2, 9, 3],
#     [7, 2, 3, 2, 1, 3, 1],
#     [1, 1, 3, 1, 7, 1, 2],
#     [4, 1, 2, 3, 4, 1, 2],
#     [3, 3, 1, 2, 3, 4, 1],
#     [1, 5, 2, 9, 4, 7, 0],
# ]
C = int(input())
for _ in range(C):

    N = int(input())
    cache = [[-1 for _ in range(N)] for _ in range(N)]

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    def jump(y, x):
        # 기저 사례 아웃오브 래인지
        if not 0 <= y <= N - 1 or not 0 <= x <= N - 1:
            return 0
        # 기저 사례 도착
        if y == N - 1 and x == N - 1:
            return 1
        # -1 이 아니면 이미 도착
        if cache[y][x] != -1:
            return cache[y][x]
        # 지금 칸의 움직이는 칸수?
        jumpsize = board[y][x]
        # 재귀로 불러오기 cache 에 저장
        cache[y][x] = jump(y + jumpsize, x) or jump(y, x + jumpsize)
        return cache[y][x]

    if jump(0, 0) == 0:
        print("NO")

    elif jump(0, 0) == 1:
        print("YES")

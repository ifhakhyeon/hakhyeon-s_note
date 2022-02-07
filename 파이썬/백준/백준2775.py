import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    # k는 층
    k = int(input())
    # n은 호수
    n = int(input())
    cache = [[-1 for _ in range(n)] for _ in range(k)]

    def solve(y, x):
        # y 가 제일 아래 0층 이면 인덱스로 치면 높이 만큼이면
        if y == k:
            # x+1 반환 호수는 1부터 시작이므로
            return x+1
        # x가 0이면 즉 왼쪽에 붙어있으면 무조건 1
        if x == 0:
            return 1
        # -1이 아니면 그 값 리턴
        if cache[y][x] != -1:
            return cache[y][x]
        else:
            # 아니면 이건데 찾고자 하는 지점이 우상 이니까 x 는 빼면서
            # y는 더하면서 탐색
            cache[y][x] = solve(y + 1, x) + solve(y, x - 1)
        return cache[y][x]
    # 여기도 위치가 우상 이니까 y의 시작 인덱스는 0임
    print(solve(0, n-1))

    #전체적으로 인덱스 주의가 필요..
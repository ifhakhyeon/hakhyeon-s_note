import sys
input = sys.stdin.readline

#범위 체크 함수
def Check(r, c, R, C):
    return r < 0 or r >= R or c < 0 or c >= C

def solution():
    R, C = map(int, input().split())
    diamond = [input().strip() for _ in range(R)]
    # ur = [[-1 for _ in range(750)] for _ in range(750)]
    # ul = [[-1 for _ in range(750)] for _ in range(750)]
    # dr = [[-1 for _ in range(750)] for _ in range(750)]
    # dl = [[-1 for _ in range(750)] for _ in range(750)]

    ur = [[0 for _ in range(C)] for _ in range(R)]
    ul = [[0 for _ in range(C)] for _ in range(R)]
    dr = [[0 for _ in range(C)] for _ in range(R)]
    dl = [[0 for _ in range(C)] for _ in range(R)]

    # 상단이동 즉 ur과 ul은 위의 정보를 반영하므로 위의 메모리제이션+1
    # 로 저장하도록 한다.
    for i in range(R):
        for j in range(C):
            if diamond[i][j] == '1':
                if Check(i, j, R, C):
                    pass
                if Check(i-1, j+1, R, C):
                    ur[i][j] = 1
                elif not Check(i-1, j+1, R, C):
                    ur[i][j] = ur[i-1][j+1] + 1

                if Check(i-1, j-1, R, C):
                    ul[i][j] = 1
                elif not Check(i-1, j-1, R, C):
                    ul[i][j] = ul[i - 1][j - 1] + 1

    for i in range(R-1, -1, -1):
        for j in range(C):
            if diamond[i][j] == '1':
                if Check(i, j, R, C):
                    pass
                # 반영할 위의 범위가 없으면 그냥 1을 저장한다. 이하동문.
                if Check(i+1, j+1, R, C):
                    dr[i][j] = 1

                elif not Check(i+1, j+1, R, C):
                    dr[i][j] = dr[i+1][j+1] + 1

                if Check(i+1, j-1, R, C):
                    dl[i][j] = 1
                elif not Check(i+1, j-1, R, C):
                    dl[i][j] = dl[i + 1][j - 1] + 1

    # print('ul', ul)
    # print('ur', ur)
    # print('dl', dl)
    # print('dr', dr)
    ans = 0
    for y in range(R):
        if ans == (min(R, C) + 1) // 2:
            return ans
        for x in range(C):
            if ans == (min(R, C) + 1) // 2:
                return ans
            # 여기서 그 부분에서 만들 수 있는 최대 삼각형의 크기보다는
            # 여태껏 저장된 정보중 가장 큰 삼각형을 만들 수 있는 것을 탐색한다.
            # 그게 더 시간이 빠름!
            maxpoint = min(dl[y][x], dr[y][x])
            if maxpoint < ans:
                continue
            for k in range(maxpoint, 0, -1):
                if k < ans:
                    continue
                if not Check(y+2*(k-1), x, R, C):
                    if ul[y+2*(k-1)][x] >= k and ur[y+2*(k-1)][x] >= k:
                        ans = max(ans, k)
                        break
    return ans


print(solution())
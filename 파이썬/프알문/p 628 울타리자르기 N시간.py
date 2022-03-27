import sys
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    h.append(int(input()))

def solvestack(h):
    remaining = []
    h.append(0)
    ret = 0
    for i in range(len(h)):
        # 남아있는게 있고 최근 저장된 남아있는게 새로 들어온것보다 더 클때
        # 즉 더 작은 사각형이 최대 넓이를 막고 있을 때
        while remaining and h[remaining[-1]] >= h[i]:
            # j는 이전까지 최대 높이
            j = remaining.pop(-1)
            # 비어있으면 0부터 가로가 됨
            if not remaining:
                width = i
            # 비어있지 않으면 이전것의 영향
            else:
                width = i - remaining[-1] - 1
            # 넓이 갱신
            ret = max(ret, h[j] * width)
        remaining.append(i)
    return ret
print(solvestack(h))
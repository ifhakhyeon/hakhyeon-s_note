import sys
input = sys.stdin.readline
# key = lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)
# list = list(map(int, f.readline().split()))

INF = 9876543210
# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# Y = int(f.readline())
n = int(input())
dist = []
for _ in range(n):
    # dist.append(list(map(int, f.readline().split())))
    dist.append(list(map(int, input().split())))

cache_deep = 5
cache = [[-1 for _ in range((1 << (n+1)))] for _ in range(n+1)]

def dp(here, visited):
    if visited == (1 << n)-1:
        # 다시 제자리로 돌아가야함
        # 5개 면 2진수 11111는 31 임 32 는 100000
        # 1<<0 = 1 (0b0), 1<<1 = 2 (0b1), 1<<2 = 4 (0b10)...
        return dist[here][0] or INF
    # 1의 개수 새기 .b('1') 1의 개수는 방문한 도시의 수임.

    if cache[here][visited] > 0:
        return cache[here][visited]

    ret = INF

    for next in range(n):
        # n번째 수가 있나 없나 확인 할 때 (0이면 없고, 1 이상이면 있는 것)
        # print(bin(0b *1* 010 & (1 << 3)))  #  0b *1* 000
        if dist[here][next] == 0 or (visited & (1 << next)) != 0:
            continue
        ret = min(ret, dp(next, (1 << next) | visited) + dist[here][next])

    cache[here][visited] = ret
    return ret

print(dp(0, 1 << 0))
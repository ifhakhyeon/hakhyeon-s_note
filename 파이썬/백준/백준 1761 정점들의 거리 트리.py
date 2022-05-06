import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 17 # 2^20 = 1,000,000

n = int(input())
parent = [[[0, 0] for _ in range(LOG)] for _ in range(n + 1)]  # 부모 노드 정보
d = [0] * (n + 1)                           # 각 노드까지의 깊이
c = [0] * (n + 1)                           # 각 노드의 깊이가 계산되었는지 여부
graph: list[list[int]] = [[] for _ in range(n + 1)]          # 그래프(graph) 정보
dist = {}

for _ in range(n - 1):
    a, b, k = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist[f'{a}{b}'] = k
    dist[f'{b}{a}'] = k


def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0][0] = x
        parent[y][0][1] = dist[f'{y}{x}']
        dfs(y, depth + 1)


# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0)   # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            # parent[j의][2**i 번째 부모] = parent[parent[j의][i - 1 번째 부모의][2**(i - 1) 번째 부모]
            parent[j][i][0] = parent[parent[j][i - 1][0]][i - 1][0]
            parent[j][i][1] += (parent[parent[j][i - 1][0]][i - 1][1] + parent[j][i - 1][1])
        # for i in parent:
        #     print(i)
        # print('---')

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    ret = 0
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    # print(parent[b])
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            # print(b, parent[b][i])
            ret += parent[b][i][1]
            b = parent[b][i][0]

            # print(ret, parent[b][i][1], b, i)
    # 부모가 같아지도록
    # print(a, b)
    if a == b:
        return ret
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i][0] != parent[b][i][0]:
            # print(i, ret)
            ret += parent[a][i][1]
            ret += parent[b][i][1]
            a = parent[a][i][0]
            b = parent[b][i][0]
    ret += parent[a][i][1]
    ret += parent[b][i][1]

    # 이후에 부모가 찾고자 하는 조상
    return ret


set_parent()

# for i in parent:
    # print(i[:5])

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
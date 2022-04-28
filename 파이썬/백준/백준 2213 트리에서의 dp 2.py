import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
score = list(map(int, input().split()))
score = [0] + score                     # score 후처리
tree: list[list[int]] = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cache = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)               # max value 방문 list
visited_ = [False] * (n+1)              # max path 방문 list
path = []                               # max path 저장


# cache[?][0] 은 선택할때 최대값 cache[?][1] 선택 안할때의 최대값
def dfs(node: int):
    visited[node] = True
    cache[node][0] = score[node]
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            # 선택 했으면 그 자식 노드들은 무조건 미선택
            cache[node][0] += cache[i][1]
            # 선택을 안했으면 자식들은 선택 혹은 미선택
            cache[node][1] += max(cache[i][0], cache[i][1])


def dfs_(node: int, choosen: bool):
    visited_[node] = True
    # 지금 node를 방문 함
    if choosen:
        # 경로 추가
        path.append(node)
        for i in tree[node]:
            # 이전에 방문을 안했으면
            if not visited_[i]:
                # 방문 안한상태로 dfs_
                dfs_(i, False)
    # 지금 노드를 방문 안함
    else:
        for i in tree[node]:
            # 아직 방문을 안했으면
            if not visited_[i]:
                # 골랐을때가 크거나 같을 때
                if cache[i][0] >= cache[i][1]:
                    dfs_(i, True)
                # 안고른게 더 클 때
                else:
                    dfs_(i, False)
    return


dfs(1)
dfs_(1, True if cache[1][0] >= cache[1][1] else False)
# print(cache)
# print(tree)
path.sort()
print(max(cache[1][0], cache[1][1]))
print(*path)
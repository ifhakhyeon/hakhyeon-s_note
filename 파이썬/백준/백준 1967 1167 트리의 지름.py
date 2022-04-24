import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(1, n+1):
    a = tuple(map(int, input().split()))

    for j in range(1, len(a)-1, 2):
        tree[a[0]].append((a[j], a[j+1]))

# plus는 여태껏 지나온 가중치들을 저장함
plus = [0] * (n+1)
k = [1]
go = deque(k)
_max = [-1, -1]
while go:
    do = go.popleft()
    for i in tree[do]:
        # plus[i[0]] 이 0이여야 안지나온 길 -1 이면 루트이므로 스킵
        if plus[i[0]] == 0 and i[0] != 1:
            plus[i[0]] += i[1] + plus[do]
            go.append(i[0])

# 가장 먼 것을 찾고 idx를 찾음
a = plus.index(max(plus))

# print(plus, a)
plus = [0] * (n+1)
k = [a]
go = deque(k)
_max = [-1, -1]
while go:
    do = go.popleft()
    for i in tree[do]:
        if plus[i[0]] == 0 and i[0] != a:
            plus[i[0]] += i[1] + plus[do]
            go.append(i[0])

ans = max(plus)
# 한번 더 진행
# print(plus)
print(ans)

# 함수로 만들어서 쓰는게 훨씬 편할듯

# 다른 풀이
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(1, n+1):
    a = tuple(map(int, input().split()))

    for j in range(1, len(a)-1, 2):
        tree[a[0]].append((a[j], a[j+1]))

def bfs(start):
    visit = [-1] * (n + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in tree[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

# 트리의 지름은 임의의 노드에서 가장 먼 노드를 찾고 그 노드에서 다시한번 제일 먼 노드를 찾는 것이다.

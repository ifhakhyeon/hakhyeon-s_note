import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cache = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    cache[node][0] = 1
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            # 자식이 얼리어답터 여도되고 아니여도됨
            cache[node][0] += min(cache[i][0], cache[i][1])
            # 자식은 꼭 얼리 어답터 여야함
            cache[node][1] += cache[i][0]
dfs(1)
print(min(cache[1][0], cache[1][1]))
'''
cache[i][0] 에는 i 노드가 얼리어답터일 때의 서브 트리에서 얼리어답터의 최소값
cache[i][1] 에는 i 노드가 얼리어답터가 아닐 때의 서브트리에서 얼리어답터의 최소값을 갱신해주면 된다.
a를 부모노드로 갖는 b, c 자식 노드가 있을 때
a 가 얼리어답터일 경우 자식 노드 b 나 c 는 얼리어답터여도 되고 아니어도 된다. 
하지만 자식노드 중 하나라도 얼리어답터가 아닐 경우 a 는 무조건 얼리어답터이어야 한다는 점을 생각하고
문제를 풀면 해결할 수 있다.
'''
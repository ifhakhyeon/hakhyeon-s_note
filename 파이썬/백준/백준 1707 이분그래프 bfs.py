import sys
input = sys.stdin.readline

def bfs():
    part_1 = (1 << V) - 1
    part_2 = (1 << V) - 1

    for i in range(V):
        # 정점에 간선이 없으면 그 정점은 있으나 마나 비트르 꺼줌
        if not graph[i]:
            visited[i] = True
            part_1 ^= (1 << i)

    # 여러개의 이분그래프가 있을경우를 대비
    # 이분그래프가 2개면 그걸합쳐도 이분그래프
    for start in to_go:
        if not visited[start]:
            part_1 ^= (1 << start)
            go = []
            go.append((start, 0))
            # 방문함
            visited[start] = True
            while go:
                where, part = go.pop()
                for i in graph[where]:
                    # 방문안했으면 현제 상태의 반대편 비트를 꺼줌
                    if not visited[i]:
                        visited[i] = True
                        go.append((i, (part+1) % 2))
                        if part == 0:
                            part_2 ^= (1 << i)
                        else:
                            part_1 ^= (1 << i)
                    # 방문했던 것을 방문하려는데
                    # 현제 상태의 비트에서 그 자리가 꺼져있으면 그건 이분그래프가 아님
                    else:
                        if part == 0:
                            if part_1 & (1 << i) == 0:
                                return False
                        else:



                            if part_2 & (1 << i) == 0:
                                return False

    if part_1 ^ part_2 != (1 << V) - 1:
        return False
    else:
        return True


C = int(input())
for _ in range(C):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    visited = [False for _ in range(V)]
    to_go = []
    for _ in range(E):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        to_go.append(u)
        to_go.append(v)
    # 중복 제거
    to_go = list(set(to_go))
    if bfs():
        print('YES')
    else:
        print('NO')

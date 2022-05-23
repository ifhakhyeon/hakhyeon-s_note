# 최소 스패닝 트리
import sys
import heapq
from random import randint

input = sys.stdin.readline

# Kruskal 알고리즘
'''
간선들을 정렬
간선이 잇는 두 정점의 root를 찾는다.
다르다면 하나의 root를 바꾸어 연결 시켜준다.

root를 저장하는 Vroot 배열을 생성한다. (여기서 root는 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장)
간선들(Elist)을 가중치 기준으로 정렬한다.
간선들이 이은 두 정점을 find함수를 통해 두 root(sRoot, eRoot)를 찾는다.
두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
가중치를 더한다.
'''

V, E = map(int, input().split())
a = randint(1, 2)
if a == 1:
    Vroot = [i for i in range(V + 1)]
    Elist = []
    for _ in range(E):
        Elist.append(list(map(int, input().split())))

    Elist.sort(key=lambda x: x[2])


    def find(x):
        if x != Vroot[x]:
            Vroot[x] = find(Vroot[x])
        return Vroot[x]


    answer = 0
    for s, e, w in Elist:
        sRoot = find(s)
        eRoot = find(e)

        if sRoot != eRoot:
            if sRoot > eRoot:
                Vroot[sRoot] = eRoot
            else:
                Vroot[eRoot] = sRoot
            answer += w

    print(answer)
    # Prim 알고리즘
    '''
    임의의 정점을 선택
    해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
    최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.

    visited: 방문여부를 확인
    Elist: 간선을 저장
    heap: 현재 그래프에서 짧은 경로를 선택
    현재 그래프에서 가장 짧은 간선을 골라 방문하지 않은 정점이라면 선택한다.
    '''
else:
    visited = [False] * (V + 1)
    Elist = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        Elist[s].append([w, e])
        Elist[e].append([w, s])

    answer = 0
    cnt = 0
    # 처음은 비용은 0 시작은 1로 시작임.
    heap = [[0, 1]]
    while heap:
        if cnt == V:
            break
        w, s = heapq.heappop(heap)
        if not visited[s]:
            visited[s] = True
            answer += w
            cnt += 1
            for i in Elist[s]:
                if not visited[i[1]]:
                    heapq.heappush(heap, i)

    print(answer)
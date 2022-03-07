import sys

input = sys.stdin.readline
# key=lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)
# list = list(map(int, f.readline().split()))

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# C = int(f.readline())
C = int(input())
for _ in range(C):
    # n, m = map(int, f.readline().split())
    n, m = map(int, input().split())
    # friends = list(f.readline().split())
    friends = list(input().split())
    caneat = [[] for _ in range(n)]
    eaters = [[] for _ in range(m)]
    for i in range(m):
        # A = list(f.readline().split())
        A = list(input().split())
        for j in A[1:]:
            eaters[i].append(friends.index(j))
            caneat[friends.index(j)].append(i)
    best = m


    def search(edible, chosen):
        global best
        if chosen >= best:
            return
        first = 0
        # 먹을 음식이 없는 친구 찾기
        while first < n and edible[first] > 0:
            first += 1
        # 다먹을 수 있으면 return
        if first == n:
            best = chosen
            return

        for k in range(len(caneat[first])):
            # 먹을 수 있는 각 음식에 대해서 food -> int
            food = caneat[first][k]
            for L in range(len(eaters[food])):
                edible[eaters[food][L]] += 1
            search(edible, chosen + 1)
            for p in range(len(eaters[food])):
                edible[eaters[food][p]] -= 1


    edible = [0 for _ in range(n)]
    search(edible, 0)
    print(best)

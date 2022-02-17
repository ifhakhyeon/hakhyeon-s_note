import sys
input = sys.stdin.readline
N, M = map(int, input().split())
def printret(ret):
    for i in ret:
        print(i, end=' ')
    print()
def choose(N, M, ret):

    if len(ret) == M:
        printret(ret)
        return

    for i in range(1, N+1):
        if i not in ret :
            choose(N, M, ret+[i])

choose(N,M,[])
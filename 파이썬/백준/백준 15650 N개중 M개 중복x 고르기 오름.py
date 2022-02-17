import sys
input = sys.stdin.readline
N, M = map(int, input().split())
def printret(ret):
    for i in ret:
        if i != 0:
            print(i, end=' ')
    print()

def choose(N, M, ret):

    if len(ret) == M+1:
        printret(ret)
        return

    for i in range(max(1, max(ret)), N+1):
        if i not in ret :
            choose(N, M, ret+[i])

choose(N,M,[0])
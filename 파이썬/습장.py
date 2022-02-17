import sys
input = sys.stdin.readline
N, M = map(int, input().split())
def printret(ret):
    for i in ret:
        if i != 0:
            print(i, end=' ')
    print()

def choose(N, M, ret):

    if len(ret) == M:
        printret(ret)
        return

    for i in range(1, N+1):
        choose(N, M, ret+[i])

choose(N,M,[])
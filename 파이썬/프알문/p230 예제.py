import sys
input = sys.stdin.readline

# 단순 전체 탐색
def lis(A):
    if A.empty():
        return 0
    ret = 0
    for i in range(len(A)):
        B=[]
        for j in range(len(A)):
            if A[i] < A[j]:
                B.append(j)
        ret = max(ret, 1+lis(B))
    return ret

# 동적 계획법
C = int(input())
for _ in range(C):
    n = int(input())
    S = list(map(int, input().split()))
    cache = [-1 for _ in range(n+1)]
    def lis2(start):
        if cache[start] != -1:
            return cache[start]
        ret = 1
        for Next in range(start+1, n):
            if S[start] < S[Next]:
                ret = max(ret, lis2(Next)+1)
        return ret
    Max = 0
    for i in range(n):
        Max = max(Max, lis2(i))
    print(Max)
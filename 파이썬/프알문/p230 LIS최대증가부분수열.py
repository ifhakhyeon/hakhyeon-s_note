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
        cache[start] = 1
        for Next in range(start+1, n):
            if S[start] < S[Next]:
                cache[start] = max(cache[start], lis2(Next)+1)
        return cache[start]
    Max = 0
    for i in range(n):
        Max = max(Max, lis2(i))
    print(Max)

C = int(input())

# 마지막 for 문을 빼줌
def lis3(start):
    if cache[start+1] != -1:
        return cache[start+1]
    cache[start + 1] = 1
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            cache[start + 1] = max(cache[start + 1], lis3(next)+1)

    return cache[start + 1]

for _ in range(C):
    n = int(input())
    S = list(map(int, input().split()))
    cache = [-1 for _ in range(n+2)]
    # lis의 길이 증가에 영향을 미치지 않을라면 -무한대 여야함
    S.append(-978654321)

    # S[-1] 은 추가된거니까 길이를 1 빼줌
    print(lis3(-1)-1)
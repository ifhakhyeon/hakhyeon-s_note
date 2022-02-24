n = int(input())
S = list(map(int, input().split()))
cache = [[-1, -1] for _ in range(n + 1)]

def lis2(mid, type):
    if cache[mid][type] != -1:
        return cache[mid][type]

    cache[mid][type] = 1

    if type == 0:
        for start in range(mid, -1, -1):
            if S[start] < S[mid]:
                cache[mid][0] = max(cache[mid][0], lis2(start, 0) + 1)

    elif type == 1:
        for end in range(mid + 1, n):
            if S[mid] > S[end]:
                cache[mid][1] = max(cache[mid][1], lis2(end, 1) + 1)

    return cache[mid][type]


Max = 0
for i in range(n):
    a = lis2(i, 0)
    b = lis2(i, 1)
    Max = max(Max, a + b - 1)
print(Max)
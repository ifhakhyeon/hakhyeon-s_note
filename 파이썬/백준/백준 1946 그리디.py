import sys
input = sys.stdin.readline

# 1
C = int(input())
for _ in range(C):
    n = int(input())
    p = [tuple(map(lambda x:n-int(x)+1, input().split())) for _ in range(n)]

    p.sort(key=lambda x: x[0])
    ans = [p[0][1]]
    for i in range(1, n):
        a = p[i][1]
        while ans:
            if ans[-1] < a:
                ans.pop()
            else:
                break
        ans.append(a)
    print(len(ans))

# 2
C = int(input())
for _ in range(C):
    n = int(input())
    p = [tuple(map(lambda x:n-int(x)+1, input().split())) for _ in range(n)]

    p.sort(key=lambda x: x[0], reverse=True)
    ans = 1
    _max = p[0][1]
    for i in range(1, n):
        if _max < p[i][1]:
            ans += 1
            _max = p[i][1]
    print(ans)

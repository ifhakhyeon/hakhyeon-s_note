import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
for i in range(n-1):
    a = list(map(int, input().split()))
    m = m+a
    m.sort()
    m = m[n:]
# 음 ... 조금 허무하네
print(m[0])

'''
import sys
import math
input = sys.stdin.readline

n = int(input())
m = []
for i in range(n):
    m.append(tuple(map(int, input().split())))

ll = [n-1] * n
for _ in range(n):
    a = -math.inf
    for i in range(n):
        if m[ll[i]][i] > a:
            a = m[ll[i]][i]
            idx = i
    ans = a
    ll[idx] -= 1
print(ans)

틀린정답이나 아이디어는 좋았던거 같다.
'''
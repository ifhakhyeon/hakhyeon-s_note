import sys
input = sys.stdin.readline

C = int(input())
s = []
for _ in range(C):
    s.append(input().rstrip())
ans = 0
for i in s:
    i = i.replace('for', '1')
    i = i.replace('while', '1')
    ret = i.count('1')
    ans = max(ans, ret)
print(ans)
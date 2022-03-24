import sys
input = sys.stdin.readline

mod = 10 ** 9 + 7
n = int(input())
# n = 3
numlist = list(map(int, input().split()))
# numlist = [7,3,2,1]
triangle = [[0] * (i + 2) for i in range(n + 1)]

triangle[0][0] = 1
triangle[0][1] = 0
for i in range(1, n+1):
    triangle[i][0] = 1
    for j in range(1, i+1):
        triangle[i][j] = (j + 1) * (triangle[i - 1][j] + triangle[i - 1][j - 1]) % mod
    triangle[i][i + 1] = 0
# for i in triangle:
#     print(i)
ans = [0] * (n + 1)
ans[0] = numlist[0]
for i in range(n):
    # print(ans)
    for j in range(1, i+2):
        ans[j] = (ans[j] + triangle[i][j - 1] * numlist[i + 1]) % mod
# print(ans)
ret = ",".join(map(str, ans))
print(f'GGG<{ret}>')
#
# a1 = var('a1')
# a2 = var('a2')
# a3 = var('a3')
# a4 = var('a4')
# a5 = var('a5')
# a6 = var('a6')
# a0 = var('a0')
# x = var('x')
# f(x) = a0 + a1*x + a2*(x**2) + a3 * (x**3) + a4 * (x**4) + a5 * (x**5) + a6*(x**6)
# g(x) = f(x+1) - f(x)
# h(x) = g(x+1) - g(x)
# i(x) = h(x+1) - h(x)
# j(x) = i(x+1) - i(x)
# k(x) = j(x+1) - j(x)
# l(x) = k(x+1) - k(x)
# print(f(0))
# print(expand(g(0)))
# print(expand(h(0)))
# print(expand(i(0)))
# print(expand(j(0)))
# print(expand(k(0)))
# print(l(0))
# 1
# 1 2
# 1 6 6
# 1 14 36 24
# 1 30 150 240 120
# 1 62 540 1560 1800 720 규칙...???
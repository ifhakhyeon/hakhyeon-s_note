import sys
import math
sys.setrecursionlimit(4010)
input = sys.stdin.readline

N = int(input())
new = list(map(int, input().split()))
mod = (10**9) + 7
ans = []
#  * new[k]  행렬 계산?
cache = sum(math.factorial(k)//math.factorial(k-i)for k in range(i+1, N+1))
cache = [[0]*(N+1) for _ in range(N+1)]

while True:
    # print(arr)
    if N == 0:
        ans.append(str(new[0]))
        break
    if N == 1:
        ans.append(str(new[0]))
        ans.append(str(new[1]))
        break
    else:
        ans.append(str(new[0]))
        for i in range(N):
            new[i] = (sum(math.factorial(k)//math.factorial(k-i) * new[k] for k in range(i+1, N+1))//(math.factorial(i))) % mod
        N -= 1

result = ','.join(ans)
print(f'GGG<{result}>')


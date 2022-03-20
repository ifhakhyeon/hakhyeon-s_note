import sys
import math
sys.setrecursionlimit(4010)
input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().split()))

def comb(n, m):
    up = math.factorial(n)
    down = (math.factorial(n - m)) * (math.factorial(m))
    return up // down

ans = []
def solve(N, arr):
    if N == 0:
        ans.append(str(arr[0]))
        return
    if N == 1:
        ans.append(str(arr[0]))
        ans.append(str(arr[1]))
        return
    else:
        ans.append(str(arr[0]))
        new = [0 for _ in range(N)]
        for i in range(1, N + 1):
            if arr[i] != 0:
                for j in range(i):
                    new[j] += (arr[i] * comb(i, j))
        return solve(N - 1, new)

solve(N, nlist)
result = ','.join(ans)
print(f'GGG<{result}>')